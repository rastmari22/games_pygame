from Platforma import Platforma
from Ball import Ball
from Wall import Wall
from Block import Block
from Coll import Collision
import pygame


def reset_game(screen):
    rows = 3
    columns = screen.get_width() // 110 + 1
    wall = Wall([Block(screen, i, j) for i in range(columns) for j in range(rows)])
    platform = Platforma(screen)
    ball = Ball(screen)
    collision = Collision(ball, wall, platform)
    return [platform,ball,wall,collision]

def play(platform,ball):
    platform.move()

    ball.upd()
def check_collisions(collision):

        collision.ball_wall()
        collision.ball_platform()
        collision.ball_blocks()

def show(wall,platform,ball):


        wall.show()
        platform.show()
        ball.show()
