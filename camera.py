import cv2
import mediapipe as mp
import time
from cgame import Cgame
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

device = 0

def getFrameNumber(start:float, fps:int):
    now = time.perf_counter() - start
    frame_now = int(now * 1000 / fps)
    return frame_now

def detection_Fingertip(img, landmarks):
    img_width, img_height = img.shape[1], img.shape[0]
    landmark_point = []
    
    for index, landmark in enumerate(landmarks.landmark):
        if landmark.visibility < 0 or landmark.presence < 0:
            continue
        landmark_x = min(int(landmark.x * img_width), img_width - 1)
        landmark_y = min(int(landmark.y * img_height), img_height - 1)
        landmark_z = landmark.z

        landmark_point.append([landmark_x, landmark_y, landmark_z])
    
    cv2.circle(img, (landmark_point[8][0], landmark_point[8][1]), 7, (0, 0, 255), -1)
    point = [landmark_point[8][0],landmark_point[8][1] ]
    return point

def main():
    global device
    cap = cv2.VideoCapture(device)
    fps = cap.get(cv2.CAP_PROP_FPS)
    wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    game = Cgame()

    print("Size:", ht, "x", wt, "/Fps: ", fps)

    start = time.perf_counter()
    frame_prv = -1

    cv2.namedWindow('MediaPipe Hands', cv2.WINDOW_NORMAL)
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
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    point = detection_Fingertip(frame, hand_landmarks)
                    game.setPoint(point[0], point[1])
            cv2.imshow('MediaPipe Hands', frame)
            game.exe()
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()

if __name__ == '__main__':
    main()
