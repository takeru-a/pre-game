import pygame as pg
from pygame import mixer

class Cgame:
    screen_w = 640
    screen_h = 480
    img = pg.image.load("./imgs/penpen2.png")
    img_w = img.get_width()
    img_h = img.get_height()
    def __init__(self, x=0, y=0):
        pg.init()
        self.x = x
        self.y = y
        self.screen = pg.display.set_mode((self.screen_w,self.screen_h))
        self.screen.fill((255,255,255))
        pg.display.set_caption("cgame")
        font = pg.font.SysFont(None,50)
        self.message = font.render("Hello!",False, (0,0,0))
        self.sound = mixer.Sound("./sounds/bird01.mp3")
        self.sound.set_volume(0.05)
    def setPoint(self, x, y):
        self.x = x
        self.y = y
    def exe(self): 
        self.screen.fill((255,255,255))
        self.screen.blit(self.message, (30, 50))
        if self.x >= self.screen_w-self.img_w:
            self.x = self.screen_w-self.img_w
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.y >= self.screen_h-self.img_h:
            self.y = self.screen_h-self.img_h
        self.screen.blit(self.img, (self.x, self.y))
        pg.display.update()

game = Cgame()
game.exe()








    