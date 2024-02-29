import pygame.draw
# from main import src as src
from Settings import Settings
s=Settings()
WIDTH=870
peach_puff = (255, 218, 185)
class Platforma():
    def __init__(self,src):
    #     self.reset(src)
    # def reset(self,src):
        self.speed=10
        self.napr = 0
        self.clr = (255, 165, 0)
        self.w = 200
        self.h = 20
        self.height=s.HEIGHT
        self.width=s.WIDTH
        self.x = WIDTH // 2 - self.w // 2
        self.y = 410
        self.src = src
        # self.reset(src)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    def show(self):#y
        # pl=pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(self.src,self.clr,self.rect,width=0)

    def move(self):#y
        pr = pygame.key.get_pressed()
        # для передвижения платформы
        self.napr=0
        if pr[pygame.K_RIGHT] and self.x + self.w <= WIDTH:
            self.rect.x += self.speed
            self.napr=1
        elif pr[pygame.K_LEFT] and self.x >= 0:
            self.rect.x -= self.speed
            self.napr = -1

    def draw_buttons(self):
        font = pygame.font.Font(None, 36)

        text = font.render("Start", True, (0, 0, 0))
        text_rect = text.get_rect(center=(50, self.height - 50))
        pygame.draw.rect(self.src, (0, 255, 0), (0, self.height - 100, 100, 100))
        self.src.blit(text, text_rect)

        text = font.render("Exit", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width - 50, self.height - 50))
        pygame.draw.rect(self.src, (255, 0, 0), (self.width - 100, self.height - 100, 100, 100))
        self.src.blit(text, text_rect)
    # def upd(self):
    #     self.rect.x += self.speedx
    #     self.rect.y += self.speedy