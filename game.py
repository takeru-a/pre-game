# pygameをインポート pgに名前を変更
import pygame as pg
#ミキサーのインポート
from pygame import mixer
#初期化
pg.init()
#スクリーンの設定
screen_w = 640
screen_h = 480
screen = pg.display.set_mode((screen_w,screen_h))
#背景の色の変更->RGB値で設定--デフォルトは黒色
screen.fill((255,255,255))
#スクリーンタイトルの設定
pg.display.set_caption("game")

#画像の読み込み
img = pg.image.load("./imgs/penpen2.png")
img_w = img.get_width()
img_h = img.get_height()
#座標の設定
x = 0
y = 390
#移動する距離を格納する変数
dis_x = 0
dis_y = 0

speed = 1
speedup = 0

#フォントの設定
font = pg.font.SysFont(None,50)
#メッセージの設定
message = font.render("Hello!",False, (0,0,0))

#音声の設定
sound = mixer.Sound("./sounds/bird01.mp3")
#音量の設定 0~1の値で設定
sound.set_volume(0.05)
#音声の出力
#.play(loops=num)でnum+1回音声が出力される num=-1で無限
sound.play(loops=2)

def move(x, y):
    #画像の表示
    screen.blit(img, (x, y))

#ゲームの起動のフラグ Flaseで終了する
running = True
while running:
    screen.fill((255,255,255))
    #メッセージの表示
    screen.blit(message, (30, 50))
    
    #イベントの取得
    for event in pg.event.get():
        #QUITイベントが起きると終了->ウインドを閉じる
        if event.type == pg.QUIT:
            running = False
        #キーボード入力があると実行
        if event.type == pg.KEYDOWN:
            # ”<-”が入力されると実行
            if event.key == pg.K_LEFT:
                dis_x -= speed
            # ”->”が入力されると実行
            if event.key == pg.K_RIGHT:
                dis_x += speed
            # upキーが入力されると実行   
            if event.key == pg.K_UP:
                dis_y -= speed
            # downキーが入力されると実行 
            if event.key == pg.K_DOWN:
                dis_y += speed
            # Wキーが入力されると実行
            if event.key == pg.K_w:
                speedup +=0.001
            # Sキーが入力されると実行
            if event.key == pg.K_s:
                speedup -=0.001
            # ESCキーを入力すると実行
            if event.key == pg.K_ESCAPE:
                running = False
        #キーボードを離すと実行
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                dis_x = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                dis_y = 0
            if event.key == pg.K_w or event.key == pg.K_s:
                speedup = 0
            
    x += dis_x
    y += dis_y
    if speed <= 0.1:
        speed=0.1
    speed += speedup
    #動ける範囲の指定
    if x >= screen_w-img_w:
        x = screen_w-img_w
    if x <= 0:
        x = 0
    if y <= 0:
        y = 0
    if y >= screen_h-img_h:
        y = screen_h-img_h
    move(x, y)
    #ディスプレイの更新->ディスプレイに変更を加えた場合は実行する必要がある
    pg.display.update()