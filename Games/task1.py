import pygame
import random
from Settings import Settings

pygame.init()

settings=Settings()
window=pygame.display.set_mode((settings.scr_w,settings.scr_h))
pygame.display.set_caption("First task")

bg_color=settings.bg_color

def change_color(text):
    new_bg_color= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for i in range(text.get_width()):
        text.set_at((i, 0), random.choice(colors))
    window.fill(new_bg_color)

    window.blit(text, (50, 50))
    pygame.display.flip()

pygame.time.set_timer(pygame.USEREVENT+1,500)

font = pygame.font.Font(None, 36)
text = font.render('Dynamic TEXT!', True, (255, 255, 255))

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
game=True
while game:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game = False
            pygame.quit()
            quit()

        if event.type==pygame.USEREVENT+1:
        # print(pygame.USEREVENT)
            change_color(text)

pygame.quit()
