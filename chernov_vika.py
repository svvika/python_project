import pygame
# from pygame import *
import tkinter
import sys
import json

FPS = 60
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BEIGE = (208, 176, 132)

pygame.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

text_font = pygame.font.Font(None, 11)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    sc.blit(img, (x, y))


def draw_dialogue(rect: tuple, text: str, text_x: int, text_y: int):
    pygame.draw.rect(sc, BEIGE, rect)
    draw_text(text, text_font, (0, 0, 0), text_x, text_y)


def house_action(house_name):
    if space != 0:
        house_x1 = house_name[0]
        house_x2 = house_name[0] + house_name[2]
        text1 = house_name[5][0]
        text2 = house_name[5][1]
        text3 = house_name[5][2]
        text4 = house_name[5][3]
        text5 = house_name[5][4]
        text6 = house_name[5][5]
        num = house_name[4]
        if (player_x1 > house_x1) and (player_x1 < house_x2):
            sc.blit(dwellers[num-1], (house_x2-30, 390))
            sc.blit(player_back, (player_x, 420))
            if space == 2:
                draw_dialogue((player_x - 115, 390, 165, 40), text1, player_x - 10, 395)
            elif space == 3:
                draw_dialogue((house_x2 + 20, 370, 225, 40), text2, house_x2 + 25, 375)
            elif space == 4:
                draw_dialogue((player_x - 115, 390, 195, 40), text3, player_x - 10, 395)
            elif space == 5:
                draw_dialogue((house_x2 + 20, 370, 195, 40), text4, house_x2 + 25, 375)
            elif space == 6:
                draw_dialogue((player_x - 115, 390, 195, 40), text5, player_x - 10, 395)
            elif space == 7:
                draw_dialogue((house_x2 + 20, 370, 195, 40), text6, house_x2 + 25, 375)


bg = [
    pygame.image.load("images\slide1_800600.png"),
    pygame.image.load("images\slide2_800600.png"),
    pygame.image.load("images\slide3_800600.png"),
    pygame.image.load("images\slide4_800600.png"),
    pygame.image.load("images\slide5_800600.png"),
    pygame.image.load("images\slide6_800600.png"),
]
player_right = pygame.image.load("images\player_right_100160_prozr.png")
player_left = pygame.image.load("images\player_100160.png")
player_front = pygame.image.load("images\player_front_100160.png")
player_back = pygame.image.load("images\player_back_100160.png")

dwellers = [pygame.image.load("images\dweller1_100160.png"),
            pygame.image.load("images\dweller2.png"),
            pygame.image.load("images\dweller3.png"),
            pygame.image.load("images\dweller4.png"),
            pygame.image.load("images\dweller5.png"),
            pygame.image.load("images\dweller6.png"),
            pygame.image.load("images\dweller7png"),
            pygame.image.load("images\dweller8.png"),
            pygame.image.load("images\dweller9.png")
]

# font = pygame.font.SysFont("Times New Roman", 100)
# text = font.render('Hello World', True, (255, 0, 0))

# ft_font = pygame.freetype.SysFont('Times New Roman', 80)

# def texts(score):
#  font = pygame.font.Font(None, 30)
# scoretext = font.render("Score:"+str(score), True, (255,255,255))
# sc.blit(scoretext, (500, 457))


bg_x = 0
bg_x1 = 0
player_speed = 1
player_x = 0
player_x1 = 0
space = 0
# bg_sound = pygame.mixer.Sound("sounds\_tweeting.mp3")
# bg_sound.play()

while 1:
    pygame.display.update()

    clock.tick(FPS)
    if player_x1 < 760:
        sc.blit(bg[0], (0, 0))
        # sc.blit(text, text.get_rect(center = sc.get_rect().center))
        # pygame.display.flip()
        # text_rect = ft_font.get_rect('Hello World')
        # text_rect.center = sc.get_rect().center
        # ft_font.render_to(sc, text_rect.topleft, 'Hello World', (255, 0, 0))
        # pygame.display.flip()
    elif player_x1 == 760 and keys[pygame.K_LEFT]:
        sc.blit(bg[0], (0, 0))
        player_x = 759
    elif player_x1 == 760 and keys[pygame.K_RIGHT]:
        sc.blit(bg[1], (0, 0))
        player_x = 0
    elif (player_x1 > 760) and (player_x1 < 760 * 2):
        # if player_x == 520:
        # player_x = 0
        sc.blit(bg[1], (0, 0))
    elif player_x1 == 760 * 2 and keys[pygame.K_LEFT]:
        sc.blit(bg[1], (0, 0))
        player_x = 759
    elif player_x1 == 760 * 2 and keys[pygame.K_RIGHT]:
        sc.blit(bg[2], (0, 0))
        player_x = 0
    elif (player_x1 > 760 * 2) and (player_x1 < 760 * 3):
        sc.blit(bg[2], (0, 0))
    elif player_x1 == 760 * 3 and keys[pygame.K_LEFT]:
        sc.blit(bg[2], (0, 0))
        player_x = 759
    elif player_x1 == 760 * 3 and keys[pygame.K_RIGHT]:
        sc.blit(bg[3], (0, 0))
        player_x = 0
    elif (player_x1 > 760 * 3) and (player_x1 < 760 * 4):
        sc.blit(bg[3], (0, 0))
    elif player_x1 == 760 * 4 and keys[pygame.K_LEFT]:
        sc.blit(bg[3], (0, 0))
        player_x = 759
    elif player_x1 == 760 * 4 and keys[pygame.K_RIGHT]:
        sc.blit(bg[4], (0, 0))
        player_x = 0
    elif (player_x1 > 760 * 4) and (player_x1 < 760 * 5):
        sc.blit(bg[4], (0, 0))
    elif player_x1 == 760 * 5 and keys[pygame.K_LEFT]:
        sc.blit(bg[4], (0, 0))
        player_x = 759
    elif player_x1 == 760 * 5 and keys[pygame.K_RIGHT]:
        sc.blit(bg[5], (0, 0))
        player_x = 0
    elif (player_x1 > 760 * 5) and (player_x1 < 760 * 6):
        sc.blit(bg[5], (0, 0))
    # elif (player_x1 == 520*6):
    #   player_x = 519

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sc.blit(player_right, (player_x, 420))
    elif keys[pygame.K_LEFT]:
        sc.blit(player_left, (player_x, 420))
    else:
        sc.blit(player_front, (player_x, 420))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if (i.key == pygame.K_UP) and (space == 0):
                space = 1
            elif (i.key == pygame.K_SPACE) and (space == 1):
                space = 2
            elif (i.key == pygame.K_SPACE) and (space == 2):
                space = 3
            elif (i.key == pygame.K_SPACE) and (space == 3):
                space = 4
            elif (i.key == pygame.K_SPACE) and (space == 4):
                space = 5
            elif (i.key == pygame.K_SPACE) and (space == 5):
                space = 6
            elif (i.key == pygame.K_SPACE) and (space == 6):
                space = 7
            elif (i.key == pygame.K_SPACE) and (space == 7):
                space = 0

    for i in range(1, 10):
        houses = json.loads("houses.json")
        house_action(houses[i])

    if keys[pygame.K_LEFT] and player_x1 > 0:
        player_x -= player_speed
        player_x1 -= player_speed
    elif keys[pygame.K_RIGHT] and player_x1 < 760 * 6:
        player_x += player_speed
        player_x1 += player_speed

    if (player_x == 760) and (player_x1 != 760 * 6):
        if keys[pygame.K_RIGHT]:
            player_x = 0
        elif keys[pygame.K_LEFT]:
            sc.blit(player_left, (759, 420))

    pygame.display.update()
