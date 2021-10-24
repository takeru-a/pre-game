import pygame as pg
import numpy as np

class Enemy():
    img = pg.image.load("./imgs/enemy.png")
    eximg = pg.image.load("./imgs/explosion.png")
    img_w = img.get_width()
    img_h = img.get_height()
    def __init__(self,x ,y=np.random.randint(0,481-img_h)):
        self.x = x
        self.y = y
        self.first = self.x
    def move(self,speed=1):
        self.x -= speed
        if self.x <= -1*self.img_w:
            self.x = self.first
            self.y = np.random.randint(0,481-self.img_h)
            
    def getImage(self):
        return self.img
    def setPoint(self, y):
        self.x = self.first
        self.y = y
    def getPoint(self):
        point = [self.x,self.y]
        return point
    def hit(self):
        num = np.random.randint(0,481-self.img_h)
        self.setPoint(num)
        return self.eximg