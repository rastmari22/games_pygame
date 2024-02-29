import random

import pygame
# from main import screen as src
yellow = (0, 255, 0)
WIDTH=870
HEIGHT=480
class Ball():
    def __init__(self,src):
        self.reset(src)
    def move(self,blocks,pl):
        for line in blocks:
            it_count=0
            for block in line:
                if self.rect.colliderect(block.rect):
                    if abs(self.rect.bottom-block.rect.top)<5 and self.speedy>0:
                        self.speedy*=-1
                    if abs(self.rect.top-block.bottom)<5 and self.speedy<0:
                        self.speedy*=-1
                    if abs(self.rect.right - block.left) < 5 and self.speedx > 0:
                        self.speedx *= -1
                    if abs(self.rect.left - block.right) < 5 and self.speedx < 0:
                        self.speedx *= -1
                block.rect=(0,0,0,0)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx *= -1
        if self.rect.top<0:
            self.speedy*=-1
        if self.rect.bottom>HEIGHT:
            self.g_o=-1

        if self.rect.colliderect(pl.rect):
            if abs(self.rect.bottom-pl.rect.top)<5 and self.speedy>0:
                self.speedy*=-1
                self.speedx+=pl.napr
                if self.speedx>self.max_speed:
                    self.speedx=self.max_speed
                elif self.speedx<0 and self.speedx<-self.max_speed:
                    self.speedx=-self.max_speed
            else:
                self.speedx*=-1

        self.rect.x+=self.speedx
        self.rect.y+=self.speedy

        return [self.g_o,blocks]
    def change_speed(self):#y
        self.speedx=-self.speedx
        plrnd=random.randint(-8,-1)
        otrrnd=random.randint(1,8)
        self.speedy=random.choice([plrnd,otrrnd])
    def show(self):#y
        pygame.draw.circle(self.src, self.clr,(self.rect.x+10,self.rect.y+10),self.rad)
    def upd(self):#y
        self.rect.x += self.speedx
        self.rect.y += self.speedy
    def reset(self,src):#y
        self.rad=10
        self.src=src

        self.x=WIDTH//2-2*self.rad
        self.y=370

        self.speedx = 4
        self.speedy = -4

        self.clr=(255, 255, 0)
        self.is_live=True
        # self.max_speed=5
        # self.g_o=0

        self.rect=pygame.Rect(self.x,self.y,self.rad*2,self.rad*2)
