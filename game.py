# pygameをインポート pgに名前を変更
import pygame as pg
#ミキサーのインポート
from pygame import mixer
import numpy as np

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
#座標の設定
x = 0
y = 390
dis_x = 0
speed = 1

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
            # ESCキーを入力すると実行
            if event.key == pg.K_ESCAPE:
                running = False
        #キーボードを離すと実行
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                dis_x = 0
            
    x += dis_x
    #動ける範囲の指定
    if x>=screen_w-img_w:
        x = screen_w-img_w
    if x<= 0:
        x = 0
    move(x, y)
    #ディスプレイの更新->ディスプレイに変更を加えた場合は実行する必要がある
    pg.display.update()