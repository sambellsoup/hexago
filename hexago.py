#!/usr/bin/env python

# Access pygame library
import pygame, sys
from pygame.locals import *

# Size and Title of the screen
SCREEN_TITLE = 'Hexago'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors according to the RGB codes
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Clock used to update game events and frames
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)
screen = pygame.display.set_mode((800,600))

class Game:
    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in black to display the Game
        self.game_screen = pygame.display.set_mode((width, height))





pygame.mouse.set_visible(1)
# pygame.mouse.set_cursor()

# pygame.draw.circle(screen, RED, [50, 50], 100)
enemy1 = pygame.image.load("images/enemy.png")
enemy1top = enemy1.get_height() - enemy1.get_height()
enemy1left = screen.get_width()/2 - enemy1.get_width()/2
screen.blit(enemy1, (enemy1left,enemy1top))


while True:
    clock.tick(60)
    pygame.display.update()

    # screen.fill((BLACK))
    x, y = pygame.mouse.get_pos()
    # screen.blit(cursor, (x-cursor.get_width()/2), cursor_top())
    # pygame.draw.circle(screen, RED, [350, -10], 40)


#Continuously check for key and mouse inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            shoot_y = y
            shoot_x = x
