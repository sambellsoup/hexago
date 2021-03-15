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
SCREEN_ORIGIN = 0
FPS = 60

# Colors according to the RGB codes
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
PINK  = (255,   0, 255)
YELLOW= (255, 255,   0)
PURPLE= (255,   0, 255)
TEAL  = (  0, 255, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")

# initialize pygame
pygame.init()

# initialize sound
pygame.mixer.init()

# create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hexago")
clock = pygame.time.Clock()
font_name = pygame.font.match_font('arial')

loaded = []

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
    outline_rect = pygame.Rect(x, 550, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, 550, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_red_mana_bar(surf, x, y, pct):
    if pct > 100:
        pct = 100
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct/100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, 575, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, 575, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
    if pct <= 0:
        pct = 0
        pygame.draw.rect(surf, BLACK, fill_rect)

def draw_yellow_mana_bar(surf, x, y, pct):
    if pct > 100:
        pct = 100
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct/100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, 600, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, 600, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, YELLOW, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
    if pct <= 0:
        pct = 0
        pygame.draw.rect(surf, BLACK, fill_rect)

def draw_blue_mana_bar(surf, x, y, pct):
    if pct > 100:
        pct = 100
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct/100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, 625, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, 625, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, BLUE, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
    if pct <= 0:
        pct = 0
        pygame.draw.rect(surf, BLACK, fill_rect)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = 550
        surf.blit(img, img_rect)

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
        self.rect.center = (SCREEN_WIDTH - 1189, SCREEN_HEIGHT - 455)
        self.shield = 100
        # Shoot delay for auto shoot
        self.cast_delay = 250
        self.last_cast = pygame.time.get_ticks()
        self.lives = 1
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.red_mana = 0
        self.blue_mana = 0
        self.yellow_mana = 0

    def update(self):
        # unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = self.rect.center = (SCREEN_WIDTH - 1189, SCREEN_HEIGHT - 455)
        keystate = pygame.key.get_pressed()
        # if keystate[pygame.<nameofkey>]:
            # self.<quality> = change
        # make border of screen wall
        # if self.rect.right > SCREEN_WIDTH:
            # self.rect.right = SCREEN_WIDTH
        if keystate[pygame.MOUSEBUTTONDOWN]:
            self.cast()

    def cast(self):
        now = pygame.time.get_ticks()
        # Allows for auto cast if mouse button held down
        if now - self.last_cast > self.cast_delay:
            self.last_cast = now
        mousex, mousey = pygame.mouse.get_pos()
        # Describes spawn point of spell
        spell = Spell(self.rect.centerx, self.rect.top)
        all_sprites.add(spell)
        spells.add(spell)
        cast_sound.play()
        if self.red_mana >= 1 and loaded == ['red']:
            mousex, mousey = pygame.mouse.get_pos()
            # Describes spawn point of spell
            spell = Spell(self.rect.centerx, self.rect.top)
            spell.image_orig = spell_red
            all_sprites.add(spell)
            spells.add(spell)
            cast_sound.play()
        if self.yellow_mana >= 1 and loaded == ['yellow']:
            mousex, mousey = pygame.mouse.get_pos()
            # Describes spawn point of spell
            spell = Spell(self.rect.centerx, self.rect.top)
            spell.image_orig = spell_yellow
            all_sprites.add(spell)
            spells.add(spell)
            cast_sound.play()
        if self.blue_mana >= 1 and loaded == ['blue']:
            mousex, mousey = pygame.mouse.get_pos()
            # Describes spawn point of spell
            spell = Spell(self.rect.centerx, self.rect.top)
            spell.image_orig = spell_blue
            all_sprites.add(spell)
            spells.add(spell)
            cast_sound.play()

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT + 200)

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
        self.health = 1 * self.radius

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
        if self.rect.right < 0 - 20 or self.rect.top < 0 - 20 or self.rect.bottom > 550:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width, SCREEN_WIDTH)
            self.rect.y = random.randrange(SCREEN_HEIGHT)
            # self.speedy = random.randrange(0)
            self.speedx = random.randrange(-8, -1)
            # self.speedy = random.randrange(-1, 1)
            # self.speedx = random.randrange(-3, 3)

class Spell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = spell_white
        self.type = spell_white
        if player.red_mana >= 1 and loaded == ['red']:
            self.image_orig = spell_red
            self.type = spell_red
        if player.yellow_mana >= 1 and loaded == ['yellow']:
            self.image_orig = spell_yellow
            self.type = spell_yellow
        if player.blue_mana >= 1 and loaded == ['blue']:
            self.image_orig = spell_blue
            self.type = spell_blue
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
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

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['red', 'blue', 'yellow'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = -2

    def update(self):
        self.rect.x += self.speedx
        # kill if it moves off the top of the screen
        if self.rect.right < SCREEN_ORIGIN:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Load all game graphices
background = pygame.image.load(os.path.join(img_folder, "background.png")).convert()
background = pygame.transform.scale(background, (1280,720))
background_rect = background.get_rect()

player_img = pygame.image.load(os.path.join(img_folder, "tower_n0.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)

smalln_bad = pygame.image.load(os.path.join(img_folder, "badn_1.png")).convert()

# spell_images = []
# spell_list = ['white_burst.png', 'red_burst.png', 'blue_burst.png', 'yellow_burst.png']
# for img in spell_list:
    # spell_images.append(pygame.image.load(os.path.join(img_folder, img)).convert())
spell_white = pygame.image.load(os.path.join(img_folder, "white_burst.png")).convert()
spell_red = pygame.image.load(os.path.join(img_folder, 'red_burst.png')).convert()
spell_yellow = pygame.image.load(os.path.join(img_folder, 'yellow_burst.png')).convert()
spell_blue = pygame.image.load(os.path.join(img_folder, 'blue_burst.png')).convert()

enemy_images = []
enemy_list = ['badn_1.png', 'badn_2.png', 'badn_3.png', 'blue_big_bad.png',
'blue_small_bad.png', 'red_big_bad.png', 'red_small_bad.png', 'yellow_big_bad.png',
'yellow_small_bad.png']
for img in enemy_list:
    enemy_images.append(pygame.image.load(os.path.join(img_folder, img)).convert())
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []

for i in range(1, 4):
    filename = 'death_{}.png'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

explosion_anim['player'] = []
for i in range(1, 6):
    filename = 'boom__{}.jpg'.format(i)
    img = pygame.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    # explosion_anim['player'].append(img)
    player_death_img = pygame.transform.scale(img, (64, 64))
    explosion_anim['player'].append(player_death_img)
powerup_images = {}
powerup_images['red'] = pygame.image.load(os.path.join(img_folder, 'red_boom.png')).convert()
powerup_images['blue'] = pygame.image.load(os.path.join(img_folder, 'blue_boom.png')).convert()
powerup_images['yellow'] = pygame.image.load(os.path.join(img_folder, 'yellow_boom.png')).convert()



# Load all game sounds
cast_sound = pygame.mixer.Sound(os.path.join(snd_folder, "basic_cast.wav"))
mana_sound = pygame.mixer.Sound(os.path.join(snd_folder, "mana.wav"))
ember_sound = pygame.mixer.Sound(os.path.join(snd_folder, "ember.wav"))
chill_sound = pygame.mixer.Sound(os.path.join(snd_folder, "chill.wav"))
shock_sound = pygame.mixer.Sound(os.path.join(snd_folder, "shock.wav"))
kill_sounds = []
for snd in ['hit.wav', 'kill.wav']:
    kill_sounds.append(pygame.mixer.Sound(os.path.join(snd_folder, snd)))
player_die_sound = pygame.mixer.Sound(os.path.join(snd_folder, 'quake.wav'))
pygame.mixer.music.load(os.path.join(snd_folder, 'hexago.wav'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
# bullets = pygame.sprite.Group()
spells = pygame.sprite.Group()
powerups = pygame.sprite.Group()

player = Player()
mousex, mousey = pygame.mouse.get_pos()
spell = Spell(mousex, mousey)
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
            if player.red_mana > 0 and loaded == ['red']:
                player.red_mana -= 10
                ember_sound.play()
                loaded = []
            if player.yellow_mana > 0 and loaded == ['yellow']:
                player.yellow_mana -= 10
                shock_sound.play()
                loaded = []
            if player.blue_mana > 0 and loaded == ['blue']:
                player.blue_mana -= 10
                chill_sound.play()
                loaded = []
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("red loaded")
                loaded = ['red']
            if event.key == pygame.K_2:
                print("yellow loaded")
                loaded = ['yellow']
            if event.key == pygame.K_3:
                print("blue loaded")
                loaded = ['blue']


    # Update
    all_sprites.update()

    # Check to see if a spell hit a mob
    hits = pygame.sprite.groupcollide(mobs, spells, True, True)
    spell = Spell(player.rect.centerx, player.rect.top)
    mob = Mob()
    for hit in hits:
        mob.health -= hit.radius * 200
        if spell.image_orig == spell_red:
            print('red hit')
            mob.health -= hit.radius * 4

        if mob.health <= 0:
            mob.health = 0
            score += 50
            random.choice(kill_sounds).play()
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if random.random() > 0.75:
                mana_sound.play()
                pow = Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
                print(pow.type)
                if pow.type == 'red':
                    player.red_mana += 20
                    print('red mana equals ' + str(player.red_mana))
                if pow.type == 'yellow':
                    player.yellow_mana += 20
                    print('yellow mana equals ' + str(player.yellow_mana))
                if pow.type == 'blue':
                    player.blue_mana += 20
                    print('blue mana eqauls ' + str(player.blue_mana))

        if player.red_mana == 0 and player.blue_mana == 0 and player.yellow_mana == 0:
            player.image_orig = spell_white
                # spell.image_orig = spell_red


    # Check to see if mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:

        # mobs strength based on size
        player.shield -= hit.radius * 2

        expl = Explosion(hit.rect.center, 'sm')
        random.choice(kill_sounds).play()
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            player_die_sound.play()
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            # player.lives -= 1
            player.shield = 100

    # if the player died and the explosion has finished playing
    if player.lives == 0 and not death_explosion.alive():
        running = False

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, "SCORE: " + str(score), 18, SCREEN_WIDTH / 2, 550)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_red_mana_bar(screen, 5, 5, player.red_mana)
    draw_yellow_mana_bar(screen, 5, 5, player.yellow_mana)
    draw_blue_mana_bar(screen, 5, 5, player.blue_mana)
    # draw_lives(screen, SCREEN_WIDTH - 100, 5, player.lives, player_mini_img)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
quit()
