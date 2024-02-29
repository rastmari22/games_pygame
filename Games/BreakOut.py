import pygame
import GameItems
from Settings import Settings



settings = Settings()
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT
FPS = settings.FPS
clock = pygame.time.Clock()

pygame.init()

sound1 = pygame.mixer.Sound('boom.wav')
sound2 = pygame.mixer.Sound('end.wav')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

running = True
game_started = False

platform,ball,wall,collision=GameItems.reset_game(screen)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            quit()
        if event.type==pygame.MOUSEBUTTONDOWN :
            if 0 <= event.pos[0] <= 100 and HEIGHT - 100 <= event.pos[1] <= HEIGHT:
                game_started = True
                sound1.play()
                platform, ball,wall,collision =GameItems.reset_game(screen)

            elif WIDTH - 100 <= event.pos[0] <= WIDTH and HEIGHT - 100 <= event.pos[1] <= HEIGHT:
                running = False

    screen.fill(settings.bg_color)

    if not game_started or not ball.is_live:

        font = pygame.font.Font(None, 36)
        text = font.render("Click to Start", True, settings.text_clr)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        text = font.render("Start", True, (0, 0, 0))
        text_rect = text.get_rect(center=(50, HEIGHT - 50))
        pygame.draw.rect(screen, (0, 255, 0), (0, HEIGHT - 100, 100, 100))
        screen.blit(text, text_rect)

        text = font.render("Exit", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH - 50, HEIGHT - 50))
        pygame.draw.rect(screen, (255, 0, 0), (WIDTH - 100, HEIGHT - 100, 100, 100))
        screen.blit(text, text_rect)
        if not ball.is_live:
            sound2.play()
    else:
        GameItems.play(platform,ball)
        GameItems.check_collisions(collision)
        GameItems.show(wall,platform,ball)
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)


