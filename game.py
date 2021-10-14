# pygameをインポート pgに名前を変更
import pygame as pg
#ミキサーのインポート
from pygame import mixer
#初期化
pg.init()
#スクリーンの設定
screen = pg.display.set_mode((640,480))
#背景の色の変更->RGB値で設定--デフォルトは黒色
screen.fill((255,255,255))
#スクリーンタイトルの設定
pg.display.set_caption("game")

#画像の読み込み
img = pg.image.load("./imgs/penpen.png")
#座標の設定
x = 320
y = 240

#音声の出力
mixer.Sound("./sounds/bird01.mp3").play()

#ゲームの起動のフラグ Flaseで終了する
running = True
while running:
    #画像の表示
    screen.blit(img, (x, y))
    #フォントの設定
    font = pg.font.SysFont(None,50)
    #メッセージの設定
    message = font.render("Hello!",False, (0,0,0))
    #メッセージの表示
    screen.blit(message, (30, 50))

    #イベントの取得
    for event in pg.event.get():
        #QUITイベントが起きると終了->ウインドを閉じる
        if event.type == pg.QUIT:
            running = False
    #ディスプレイの更新->ディスプレイに変更を加えた場合は実行する必要がある
    pg.display.update()