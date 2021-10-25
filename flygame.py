import pygame as pg
import time
from enemy import Enemy
from item import Item


class Flygame:
    screen_w = 960
    screen_h = 480
    back = pg.image.load("./imgs/suichu2.jpg")
    back = pg.transform.scale(back, (1920, 480))
    img = pg.image.load("./imgs/swimpen.png")
    f_img = img
    img_w = img.get_width()
    img_h = img.get_height()
    score = 0
    hp = 2
    hpflag = 0
    start_time = 0
    time = 0
    item_timer = 0
    start_time2 = 0
    
    hp_img = pg.image.load("./imgs/hp.png")
   
    
    def __init__(self, x=200, y=200):
        pg.init()
        self.x = x
        self.y = y
        self.screen =pg.display.set_mode((self.screen_w,self.screen_h))
        pg.display.set_caption("flygame")
        self.font1 = pg.font.SysFont(None,50)
        font2 = pg.font.SysFont(None,200)
        self.message = self.font1.render("HP:",False, (0,255,0))
        self.score_mg = self.font1.render("SCORE:",False, (255,0,255))
        self.gameover = font2.render("GAME OVER",False, (255,0,0))
        self.start_time = time.time()
        self.start_time2 = self.start_time
        self.init_timer = self.start_time
        self.cnt = 1
        self.enemy = Enemy(self.screen_w,200)
        self.e_list = []
        self.e_list.append(self.enemy)
        self.item = Item(self.screen_w)
        self.bg_x = 0
        
        

    def setPoint(self, flag):
        if flag:
            self.y -= 12
        else:
            self.y += 5

    def resetPoint(self):
        self.x = 200
        self.y = 200
    
    def item_get(self):
        item = self.item.getImage()
        min_point = [self.x, self.y]
        max_point = [self.x+self.img_w-8, self.y+self.img_h]
        e_up = self.item.getPoint()
        e_mid = [e_up[0],e_up[1]+item.get_height()//2]
        e_down = [e_up[0],e_up[1]+item.get_height()]
        e_back = [e_up[0]+item.get_width(),e_up[1]+item.get_height()//2]

        if min_point[0] <= e_mid[0] <= max_point[0]:
            if min_point[1] <= e_mid[1] <= max_point[1]:
                return True
        if min_point[0] <= e_up[0] <= max_point[0]:
            if min_point[1] <= e_up[1] <= max_point[1]:
                return True
        if min_point[0] <= e_down[0] <= max_point[0]:
            if min_point[1] <= e_down[1] <= max_point[1]:
                return True
        if min_point[0] <= e_back[0] <= max_point[0]:
            if min_point[1] <= e_back[1] <= max_point[1]:
                return True
        return False

    def conllision(self, e_points, e_img):
        min_point = [self.x, self.y]
        max_point = [self.x+self.img_w-8, self.y+self.img_h]
        index = 0
        for e_point in e_points:
            e_up = [e_point[0]+25,e_point[1]+8]
            e_mid = [e_point[0],e_point[1]+e_img.get_height()//2]
            e_down = [e_point[0]+25,e_point[1]+e_img.get_height()-8]
            e_back = [e_point[0]+e_img.get_width(),e_point[1]+e_img.get_height()//2]
            if min_point[0] <= e_mid[0] <= max_point[0]:
                if min_point[1] <= e_mid[1] <= max_point[1]:
                    return True, index
            if min_point[0] <= e_up[0] <= max_point[0]:
                if min_point[1] <= e_up[1] <= max_point[1]:
                    return True, index
            if min_point[0] <= e_down[0] <= max_point[0]:
                if min_point[1] <= e_down[1] <= max_point[1]:
                    return True, index
            if min_point[0] <= e_back[0] <= max_point[0]:
                if min_point[1] <= e_back[1] <= max_point[1]:
                    return True, index
            index += 1
        return False , -1
    def exe(self):
        self.score += 0.5  
        score_num = self.font1.render(f" {int(self.score)} M",False, (255,150,105))
        SCROLL = 12
        INTERVAL = 10
        INTERVAL2 = 5
        UPPER_LIMIT = 3
        SPEED = 30
        if self.start_time == self.init_timer:
            self.start_time = time.time()
            self.start_time2 = time.time()
        self.time = time.time()-self.start_time
        if int(self.time) == INTERVAL and self.cnt < UPPER_LIMIT:
            enemy = Enemy(self.screen_w)
            self.e_list.append(enemy)
            self.start_time = time.time()
            self.cnt += 1
        self.bg_x = (self.bg_x-SCROLL)%self.screen_w
        self.screen.fill((255,255,255))
        self.screen.blit(self.back, (self.bg_x,0))
        self.screen.blit(self.back, (self.bg_x-self.screen_w,0))
        self.screen.blit(self.message, (30, 20))
        self.screen.blit(self.score_mg, (500, 20))
        self.screen.blit(score_num, (640, 20))

        self.item_timer = time.time()-self.start_time2
        if int(self.item_timer) >= INTERVAL2:
            point = self.item.getPoint()
            item_img = self.item.getImage()
            self.screen.blit(item_img,(point[0],point[1]))
            self.item.move(speed=SPEED)
            if point[0] <= -1*item_img.get_width():
                self.item.setPoint()
                self.start_time2 = time.time()
                

        
        if self.x >= self.screen_w-self.img_w:
            self.x = self.screen_w-self.img_w
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        if self.y >= self.screen_h-self.img_h:
            self.y = self.screen_h-self.img_h
        self.screen.blit(self.img, (self.x, self.y))

        points = []
        for enemy in self.e_list:
            points.append(enemy.getPoint())
        enemy_img = self.enemy.getImage()
        result = self.conllision(points,enemy_img)
        if result[0]:
            self.hp -= 1
            self.screen.blit(self.e_list[result[1]].hit(),(self.x+self.img_w//2,self.y))
        if self.hp==1 and self.hpflag==0:
            self.hpflag += 1
            self.img = pg.transform.scale(self.img, (self.img_h*2, self.img_w//2))
            self.img_w = self.img.get_width()
            self.img_h = self.img.get_height()
        else:
            for enemy in self.e_list:
                points = enemy.getPoint()
                self.screen.blit(enemy_img,(points[0],points[1]))
                enemy.move(speed=SPEED)
        if self.item_get():
            self.item.setPoint()
            self.start_time2 = time.time()
            self.hp = 2
            self.hpflag = 0
        if self.hp == 1:
            self.screen.blit(self.hp_img,(90,23))
        if self.hp==2:
            self.screen.blit(self.hp_img,(90,23))
            self.screen.blit(self.hp_img,(90+self.hp_img.get_width(),23))
            self.img = self.f_img
            self.img_w = self.img.get_width()
            self.img_h = self.img.get_height()
        if self.hp <= 0:
            self.screen.blit(self.gameover,(50,200))
            pg.display.update()
            return True
        pg.display.update()
        return False