import random

import pygame
class Block():
    x_r, y_r = 110, 60
    light_cyan = (173, 216, 230)
    cl1=(144, 238, 144)
    cl2=(0, 100, 0)
    clrs=[light_cyan,cl1,cl2]
    c = random.choice(clrs)

    def __init__(self,src,i,j):
        self.x1=self.x_r*i
        self.y1=self.y_r*j
        self.w, self.h =   100, 50
        self.src=src
        self.rect=pygame.Rect(self.x1,self.y1,self.w,self.h)
        self.visible=True

    def break_visible(self):
        self.visible=False
        self.rect=pygame.Rect(0,0,0,0)
    def draw_block(self):
        if self.visible:
            return pygame.Rect(self.x1,self.y1,self.w,self.h)
    def show(self):  # y
        pygame.draw.rect(self.src, self.c, self.draw_block(), 0)
            # pygame.draw.rect(self.src, light_cyan,(self.x1,self.y1,self.w,self.h),width=0)
    # def create_bl(self,i,j):
    #     self.x1+=i*self.x_r
    #     self.y1 +=j * self.y_r
    #     return pygame.Rect(self.x1, self.y1 , self.w, self.h)

        # return pygame.Rect(self.x1+i*self.x_r,self.y1+j*self.y_r,self.w,self.h)


    # def create_blocks(self):
    #     blocks_cr = [Block(self.src,i,j) for i in range(8) for j in range(3)]
    #     for j in range(24):
    #         pygame.draw.rect(self.src, (255, 0, 0), blocks[j], 0)
    #     return blocks_cr


# for i in range(8):
#     for j in range(3):
#         first_Block.create_bl(i,j)

# first_Block=Block(screen,0,0)


