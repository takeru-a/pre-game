import pygame as pg
import numpy as np

class Item():
    HEIGHT = 481
    img = pg.image.load("./imgs/heart.png")
    img = pg.transform.scale(img,(50,50))
    img_w = img.get_width()
    img_h = img.get_height()
    def __init__(self,x ,y=np.random.randint(0,HEIGHT-img_h)):
        self.x = x
        self.y = y
        self.first = self.x
    def move(self,speed=1):
        self.x -= speed
    
    def getImage(self):
        return self.img
    def setPoint(self):
        self.x = self.first
        self.y = np.random.randint(0,self.HEIGHT-self.img_h)
    def getPoint(self):
        point = [self.x,self.y]
        return point