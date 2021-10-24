from numpy.random.mtrand import f
import cv2
import mediapipe as mp
import time
from flygame import Flygame
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
play_game = 0
device = 0
play_img = cv2.imread("./imgs/play.jpg")

def getFrameNumber(start:float, fps:int):
    now = time.perf_counter() - start
    frame_now = int(now * 1000 / fps)
    return frame_now

def pinch(img, point):
    flag = False
    points = [(point[0][0]+point[1][0])//2,(point[0][1]+point[1][1])//2]
    if abs(point[0][0]-point[1][0])<=15 and abs(point[0][1]-point[1][1])<=25:
        cv2.circle(img, (points[0], points[1]), 7, (0, 255, 255), 3)
        cv2.putText(img, "UP",(200,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        flag = True
    else :
        cv2.putText(img, "DOWN",(200,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    
    return flag
def combine(img):
    white = np.ones((img.shape), dtype=np.uint8) * 255  
     
    white[100:100+play_img.shape[0],400:400+play_img.shape[1]] = play_img
    dwhite = white
    img[dwhite!=[255, 255, 255]] = dwhite[dwhite!=[255, 255, 255]]
    cv2.putText(img, "PLAY GAME!!",(380,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
def detection_Fingertip(img, landmarks):
    global play_game
    img_width, img_height = img.shape[1], img.shape[0]
    landmark_point = []
    
    for index, landmark in enumerate(landmarks.landmark):
        if landmark.visibility < 0 or landmark.presence < 0:
            continue
        landmark_x = min(int(landmark.x * img_width), img_width - 1)
        landmark_y = min(int(landmark.y * img_height), img_height - 1)
        landmark_z = landmark.z

        landmark_point.append([landmark_x, landmark_y, landmark_z])
    
    if 100 <= landmark_point[8][1] <= 100+play_img.shape[0] :
        if 400 <= landmark_point[8][0] <= 400+play_img.shape[1]:
            play_game = 1
    cv2.circle(img, (landmark_point[8][0], landmark_point[8][1]), 7, (0, 0, 255), -1)
    cv2.circle(img, (landmark_point[4][0], landmark_point[4][1]), 7, (0, 0, 255), -1)
    
    point = [landmark_point[4],landmark_point[8]]
    flag =  pinch(img, point)
    return flag

def main():
    global play_game
    global device
    cap = cv2.VideoCapture(device)
    fps = cap.get(cv2.CAP_PROP_FPS)
    wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    game = Flygame()

    print("Size:", ht, "x", wt, "/Fps: ", fps)

    start = time.perf_counter()
    frame_prv = -1

    cv2.namedWindow('MYcamera', cv2.WINDOW_NORMAL)
    with mp_hands.Hands(
        max_num_hands = 1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as hands:
        while cap.isOpened():
            frame_now=getFrameNumber(start, fps)
            if frame_now == frame_prv:
                continue
            frame_prv = frame_now

            ret, frame = cap.read()
            if not ret:
                print("Ignoring empty camera frame.")
                
                continue
            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    
            frame.flags.writeable = False
            results = hands.process(frame)
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            flag = False
            combine(frame)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    flag = detection_Fingertip(frame, hand_landmarks)
                    if play_game == 1:
                        game.setPoint(flag)
                    
            cv2.imshow('MYcamera', frame)
            if play_game == 1:
                if game.exe():
                    play_game = 0
                    game = Flygame()
                game.setPoint(flag)
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()

if __name__ == '__main__':
    main()