# Pygame template - skeleton for a new pygame project
import pygame
import random
import os
from os import path

img_dir = path.join(path.dirname(__file__), 'images')
snd_dir = path.join(path.dirname(__file__), 'audio')

WIDTH = 800
HEIGHT = 600
FPS = 60

# define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
# screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Hexago")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load(os.path.join(img_folder, "player.png")).convert()
        # self.image.set_colorkey(RED)
        self.image = pygame.transform.scale(player_img, (800, 60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 350
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        # if keystate[pygame.K_a]:
            # movement left
            # self.speedx = -8
        # if keystate[pygame.K_s]:
            # movement right
            # self.speedx = 8
        self.rect.x += self.speedx
        # Constrained to stay on the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def cast(self):
        mousex, mousey = pygame.mouse.get_pos()
        spell = Spell(self.rect.centerx, self.rect.top)
        all_sprites.add(spell)
        spells.add(spell)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(enemy_images)
        self.image_orig = small_enemy_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .4 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        # Always appears somewhere between the left and right
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 2)
        self.speedx = random.randrange(-1, 1)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_updae = now
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
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 2)

class Spell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = spell_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = mousey
        self.rect.centerx = mousex
        cast_sound.play()


    # def update(self):
        # self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        # if self.rect.botom < 0:
        # self.kill()

# initiate pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexago")
clock = pygame.time.Clock()

# Load all game graphics
# background = pygame.image.load(path.join(img_dir, "strafield.png")).convert()
# background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "altar.png")).convert()
small_enemy_img = pygame.image.load(path.join(img_dir, "small_bad.png")).convert()
spell_img = pygame.image.load(path.join(img_dir, "boom.png")).convert()
enemy_images = []
enemy_list = ["small_bad.png"]
for img in enemy_list:
    enemy_images.append(pygame.image.load(path.join(img_dir, img)).convert())
# Load all game sounds
cast_sound = pygame.mixer.Sound(path.join(snd_dir, 'burst_attack.wav'))
hit_sound = pygame.mixer.Sound(path.join(snd_dir, 'hit.wav'))
pygame.mixer.music.load(path.join(snd_dir, 'hexago.wav'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
spells = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
score = 0
# Able to play playlist to extend music
pygame.mixer.music.play(loops=-1)

#  Game loop
running = True
while running:
    # Keep loop running at the right SPEED
    clock.tick(FPS)
    mousex, mousey = pygame.mouse.get_pos()
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.cast()


# Update
    all_sprites.update()

# check to see if a bullet hit a mob. The first true deletes mob and second true deletes spell
    hits = pygame.sprite.groupcollide(mobs, spells, True, True)
    # respawns enemies as they are hit
    for hit in hits:
        score += 10
        # Show damage against enemy in numbers above them
        hit_sound.play()
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the Player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    # pygame.sprite.collide_circle
    if hits:
        running = False

# Draw / render
    screen.fill(BLACK)
    # screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, "Score: " + str(score), 10, WIDTH / 2, 10)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
