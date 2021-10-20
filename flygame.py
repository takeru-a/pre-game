import pygame as pg
from pygame import mixer

class Flygame:
    screen_w = 960
    screen_h = 480
    back = pg.image.load("./imgs/suichu.jpg")
    back = pg.transform.scale(back, (960, 480))
    img = pg.image.load("./imgs/flypen.png")
    img_w = img.get_width()
    img_h = img.get_height()
    def __init__(self, x=0, y=200):
        pg.init()
        self.x = x
        self.y = y
        self.screen =pg.display.set_mode((self.screen_w,self.screen_h))
        #self.bg = self.back.convert_alpha() 
        self.rect_bg = self.back.get_rect()
        self.screen.fill((255,255,255))
        self.screen.blit(self.back, self.rect_bg)
        pg.display.set_caption("flygame")
        font = pg.font.SysFont(None,50)
        self.message = font.render("Hello!",False, (0,0,0))
        self.sound = mixer.Sound("./sounds/bird01.mp3")
        self.sound.set_volume(0.05)
    def setPoint(self, flag):
        self.x += 2.5
        if flag:
            self.y -= 5
        else:
            self.y += 3
    def resetPoint(self):
        self.x = 0
        self.y = 200    
    def exe(self): 
        self.screen.fill((255,255,255))
        self.screen.blit(self.back, self.rect_bg)
        #self.screen.blit(self.message, (30, 50))
        
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

game = Flygame()
game.exe()








    