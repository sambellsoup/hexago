#!/usr/bin/env python

# Pygame template - skeleton for a new pygame project
import pygame
import random
import os
import time

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
snd_folder = os.path.join(game_folder, "snd")

# initialize pygame and create window
pygame.init()
# allows for sound
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hexago")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

class Player(pygame.sprite.Sprite):
    #sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Normal size
        # self.image = player_img
        # Example of scaling
        self.image = pygame.transform.scale(player_img, (64, 64))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .5 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (SCREEN_WIDTH - 1240, SCREEN_HEIGHT / 2)
        self.shield = 100

    def update(self):
        keystate = pygame.key.get_pressed()
        # if keystate[pygame.<nameofkey>]:
            # self.<quality> = change
        # make border of screen wall
        # if self.rect.right > SCREEN_WIDTH:
            # self.rect.right = SCREEN_WIDTH

    def cast(self):
        now = pygame.time.get_ticks()
        # if now - self.last_shot > self.shoot_delay:
            # self.last_shot = now
        mousex, mousey = pygame.mouse.get_pos()
        # Describes spawn point of spell
        spell = Spell(self.rect.centerx, self.rect.top)
        all_sprites.add(spell)
        spells.add(spell)
        cast_sound.play()

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = smalln_bad
        # self.image_orig = pygame.transform.scale(smalln_bad, (32, 32))
        self.image_orig = random.choice(enemy_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .375 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        # Enemy spawns randomly across screen
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width, SCREEN_WIDTH)
        self.rect.y = random.randrange(SCREEN_HEIGHT)
        self.speedx = random.randrange(-8, -1)
        self.speedy = random.randrange(-3, 3)
        # Setup animating sprite
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right < 0 - 20 or self.rect.top < 0 - 20 or self.rect.bottom > SCREEN_HEIGHT + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width, SCREEN_WIDTH)
            self.rect.y = random.randrange(SCREEN_HEIGHT)
            # self.speedy = random.randrange(0)
            self.speedx = random.randrange(-8, -1)
            # self.speedy = random.randrange(-1, 1)
            # self.speedx = random.randrange(-3, 3)

class Spell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = spell_neutral
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.bottom = mousey
        self.rect.centerx = mousex
        # cast_sound.play()

    # def update(self):
        # Delete after 2 secs
        # time.sleep(2)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        # self.speedy = -10

    def update(self):
        # self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

# Load all game graphices
# background = pygame.image.load(os.path.join(img_folder, "file_name")).convert()
# background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(img_folder, "tower_n0.png")).convert()
smalln_bad = pygame.image.load(os.path.join(img_folder, "badn_1.png")).convert()
spell_neutral = pygame.image.load(os.path.join(img_folder, "white_boom.png")).convert()
enemy_images = []
enemy_list = ['badn_1.png', 'badn_2.png', 'badn_3.png']
for img in enemy_list:
    enemy_images.append(pygame.image.load(os.path.join(img_folder, img)).convert())

# Load all game sounds
cast_sound = pygame.mixer.Sound(os.path.join(snd_folder, "basic_cast.wav"))
kill_sounds = []
for snd in ['hit.wav', 'kill.wav']:
    kill_sounds.append(pygame.mixer.Sound(os.path.join(snd_folder, snd)))
pygame.mixer.music.load(os.path.join(snd_folder, 'hexago.wav'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
# bullets = pygame.sprite.Group()
spells = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    newmob()

score = 0

# Music repeats
pygame.mixer.music.play(loops=-1)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.cast()

    # Update
    all_sprites.update()

    # Check to see if a spell hit a mob
    hits = pygame.sprite.groupcollide(mobs, spells, True, True)
    for hit in hits:
        score += 50
        random.choice(kill_sounds).play()
        newmob()

    # Check to see if mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 2
        newmob()
        if player.shield <= 0:
            running = False

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, "SCORE: " + str(score), 18, SCREEN_WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
quit()
