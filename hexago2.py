# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

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

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load(os.path.join(img_folder, "player.png")).convert()
        # self.image.set_colorkey(RED)
        self.image = pygame.Surface((800, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
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
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # Always appears somewhere between the left and right
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 2)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 2)

class Spell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = mousey
        self.rect.centerx = mousex


    def update(self):
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

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
spells = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

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
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    # check to see if a mob hit the Player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

# Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
