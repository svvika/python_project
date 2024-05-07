import pygame
import sys

FPS = 60
WIDTH = 800  
HEIGHT = 400
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
clock = pygame.time.Clock()

bg = pygame.image.load("images\phon_probe.jpg")
player_right = pygame.image.load("images\player_right_100160_prozr.png")
player_left = pygame.image.load("images\player_100160.png")
player_front = pygame.image.load("images\player_front_100160.png")

pygame.init()

bg_x = 0
player_speed = 1
player_x = 0
bg_sound = pygame.mixer.Sound("sounds\_tweeting.mp3")
bg_sound.play()

while 1:
    sc.blit(bg, (bg_x, 0))
    sc.blit(bg, (bg_x + 800, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sc.blit(player_right, (player_x, 200))
    elif keys[pygame.K_LEFT]:
        sc.blit(player_left, (player_x, 200))
    else:
        sc.blit(player_front, (player_x, 200))


    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 750:
        player_x += player_speed

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    bg_x -= 2
    if bg_x == -800:
        bg_x = 0

    pygame.display.update()

    clock.tick(FPS)
