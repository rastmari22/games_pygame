import pygame
# points = random_points(100)
WIDTH=870
HEIGHT=480
class Collision():
    def __init__(self,ball,wall,platforma):
        self.ball=ball
        self.wall=wall
        self.platforma=platforma
        self.stop_game=False
    def ball_platform(self):
        if pygame.Rect.colliderect(self.platforma.rect,self.ball.rect):
            sound1 = pygame.mixer.Sound('mixkit-cartoon-toy-whistle-616.wav')
        # if self.ball.rect.colliderect(self.platforma.rect):
            sound1.play()
            self.ball.rect.x-=self.ball.speedx
            self.ball.rect.y -= self.ball.speedy
            self.ball.change_speed()

        # if platforma.x <= ball.x <= platforma.x + platforma.width and platforma.y - ball.y <= ball.radius:
        #     ball.dy *= -1
    def ball_blocks(self):
        for block in self.wall.arr_bl:
            if block.rect.colliderect(self.ball.rect):
                block.visible=False
                block.rect=pygame.Rect(0,0,0,0)
                self.ball.change_speed()
        if not self.wall.exist():
            self.stop_game=True
    def ball_wall(self):
        if self.ball.rect.x>=WIDTH or self.ball.rect.x<=0:
            self.ball.speedx*=-1
        if self.ball.rect.top <= 0:
            self.ball.speedy *= -1
        if self.ball.rect.bottom > HEIGHT:
            self.ball.is_live=False
            # self.stop_game=True
