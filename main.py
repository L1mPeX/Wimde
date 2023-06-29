import pygame
from sys import exit
from constants import *
from character import Character

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wimde")

clock = pygame.time.Clock()

moving_left = False
moving_right = False
moving_up = False
moving_down = False


def scale_image(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))


player_image = pygame.image.load("files/player/inactive/0.png").convert_alpha()
# player_image = pygame.transform.scale(player_image, (player_image.get_width() * SCALE, player_image.get_height() * SCALE))
player_image = scale_image(player_image, SCALE)
player = Character(100, 100, player_image)

while True:
    clock.tick(FPS)

    screen.fill(BG)

    dx = 0
    dy = 0
    if moving_left:
        dx = -SPEED
    if moving_right:
        dx = SPEED
    if moving_up:
        dy = -SPEED
    if moving_down:
        dy = SPEED
    print(f"{dx} {dy}")

    player.draw(screen)
    player.move(dx, dy)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_s:
                moving_down = False
            elif event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_d:
                moving_right = False

    pygame.display.update()
