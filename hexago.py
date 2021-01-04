#!/usr/bin/env python

# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

# Size and Title of the screen
SCREEN_TITLE = 'Hexago'
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Colors according to the RGB codes
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
PINK = (255, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
TEAL = (0, 255, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "tower_1.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT-20)

    def update(self):
        keystate = pygame.key.get_pressed()
        # if keystate[pygame.<nameofkey>]:
            # self.<quality> = change
        # make border of screen wall
        # if self.rect.right > SCREEN_WIDTH:
            # self.rect.right = SCREEN_WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "badn_1.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # Enemy spawns randomly across screen
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hexago")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # Check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    # Check to see if mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
quit()

"""
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


class Game():
    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in black to display the Game
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(BLACK)
        pygame.display.set_caption(SCREEN_TITLE)

        # Set background image of game
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player = Player("images/player.png", 375, 700, 50, 50)


        # screen.blit(cursor, (x-cursor.get_width()/2), cursor_top())

        enemy_0 = Enemy("images/enemy.png", 375, 0, 50, 50)
        # enemy_0top = enemy1.get_height() - enemy_0.get_height()
        # enemy_0left = screen.get_width()/2 - enemy_0.get_width()/2
        # screen.blit(enemy1, (enemy0left,enemy0top))
        enemy_0.SPEED *= level_speed

        enemy_1 = Enemy('images/enemy.png', self.height - 40, 400, 50, 50)
        enemy_1.SPEED *= level_speed

        enemy_2 = Enemy('images/enemy.png', 20, 200, 50, 50)
        enemy_2.SPEED *= level_speed

        # Main game loop used to update all gameplay such as movement, checks,
        # and graphices until game_over

        while not is_game_over:
            x, y = pygame.mouse.get_pos()
        # Continuously check for key and mouse inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    shoot_y = y
                    shoot_x = x
                print(event)

        # update
            all_sprites.update()

        # draw/render

        # Character appearance and movement
            all_sprites.draw(self.game_screen)
            self.game_screen.fill(BLACK)
            self.game_screen.blit(self.image, (0, 0))

            player.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 2:
                enemy1.move(self.width)
                enemy1.draw(self.game_screen)
            if level_speed > 4:
                enemy2.move(self.width)
                enemy2.draw(self.game_screen)

            if player.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You dead.', True, WHITE)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                waiting = True
                while waiting:
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.KEYUP:
                            waiting = False

            pygame.display.flip()

            clock.tick(self.TICK_RATE)


class GameObject():

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height/2)

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class Player(GameObject):
    # Sprite for the player
    def __init__ (self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        self.rect = self.image.get_rect()

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self. x_pos + self.width < other_body.x_pos:
            return False

        return True

class Enemy(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.y_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.y_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.y_pos += self.SPEED

new_game = Game('images/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

pygame.quit()
quit()
"""
