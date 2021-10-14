import pygame as pg
from pygame import mixer
#初期化
class Cgame:
    def __init__(self, x, y):
        pg.init()
        self.x = x
        self.y = y
        self.screen_w = 640
        self.screen_h = 480
        self.screen = pg.display.set_mode((self.screen_w,self.screen_h))
        self.screen.fill((255,255,255))
        pg.display.set_caption("cgame")
        self.img = pg.image.load("./imgs/penpen2.png")
        self.img_w = self.img.get_width()
        self.img_h = self.img.get_height()
        font = pg.font.SysFont(None,50)
        self.message = font.render("Hello!",False, (0,0,0))
        self.sound = mixer.Sound("./sounds/bird01.mp3")
        self.sound.set_volume(0.05)
    def exe(self): 
        self.sound.play(loops=2)
        dis_x = 0
        dis_y = 0
        running = True
        while running:
            self.screen.fill((255,255,255))
            self.screen.blit(self.message, (30, 50))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    # ”<-”が入力されると実行
                    if event.key == pg.K_LEFT:
                        dis_x -= 1
                    # ”->”が入力されると実行
                    if event.key == pg.K_RIGHT:
                        dis_x += 1
                    # upキーが入力されると実行   
                    if event.key == pg.K_UP:
                        dis_y -= 1
                    # downキーが入力されると実行 
                    if event.key == pg.K_DOWN:
                        dis_y += 1
                    if event.key == pg.K_ESCAPE:
                        running = False
                #キーボードを離すと実行
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                        dis_x = 0
                    if event.key == pg.K_UP or event.key == pg.K_DOWN:
                        dis_y = 0
            if self.x >= self.screen_w-self.img_w:
                self.x = self.screen_w-self.img_w
            if self.x <= 0:
                self.x = 0
            if self.y <= 0:
                self.y = 0
            if self.y >= self.screen_h-self.img_h:
                self.y = self.screen_h-self.img_h
            self.x += dis_x
            self.y += dis_y
            self.screen.blit(self.img, (self.x, self.y))
            pg.display.update()

game = Cgame(0,0)
game.exe()








    