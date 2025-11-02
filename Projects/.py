import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen
SCREEN_WIDTH, SCREEN_HEIGHT = 288, 512
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

# Load assets
BG = pygame.image.load("assets/background.png")
BIRD = pygame.image.load("assets/bird.png")
PIPE = pygame.image.load("assets/pipe.png")
BASE = pygame.image.load("assets/base.png")
GAME_OVER = pygame.image.load("assets/gameover.png")

# Game variables
gravity = 0.25
bird_movement = 0
bird_rect = BIRD.get_rect(center=(50, 256))

base_x = 0

pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

pipe_height = [200, 300, 400]

score = 0
font = pygame.font.Font(None, 40)

# Functions
def draw_base():
    SCREEN.blit(BASE, (base_x, 450))
    SCREEN.blit(BASE, (base_x + 288, 450))

def create_pipe():
    height = random.choice(pipe_height)
    bottom = PIPE.get_rect(midtop=(300, height))
    top = PIPE.get_rect(midbottom=(300, height - 150))
    return top, bottom

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            SCREEN.blit(PIPE, pipe)
        else:
            flip_pipe = pygame.transform.flip(PIPE, False, True)
            SCREEN.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
        return False
    return True

def show_score(score):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    SCREEN.blit(text, (10, 10))

# Game loop
game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50, 256)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    SCREEN.blit(BG, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        SCREEN.blit(BIRD, bird_rect)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Score
        score += 0.01
        show_score(int(score))
    else:
        SCREEN.blit(GAME_OVER, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

    # Base
    base_x -= 1
    if base_x <= -288:
        base_x = 0
    draw_base()

    pygame.display.update()
    CLOCK.tick(60)