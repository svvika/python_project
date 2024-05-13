import pygame
#from pygame import *
import tkinter
import sys

FPS = 60
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BEIGE = (208, 176, 132)

pygame.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
clock = pygame.time.Clock()

text_font = pygame.font.Font("mytype.ttf", 11)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    sc.blit(img, (x, y))

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
dweller1 = pygame.image.load("images\dweller1_100160.png")
dweller2 = pygame.image.load("images\dweller2.png")

#font = pygame.font.SysFont("Times New Roman", 100)
#text = font.render('Hello World', True, (255, 0, 0))

#ft_font = pygame.freetype.SysFont('Times New Roman', 80)

#def texts(score):
 #  font = pygame.font.Font(None, 30)
  # scoretext = font.render("Score:"+str(score), True, (255,255,255))
   #sc.blit(scoretext, (500, 457))


bg_x = 0
bg_x1 = 0
player_speed = 1
player_x = 0
player_x1 = 0
space = 0
#bg_sound = pygame.mixer.Sound("sounds\_tweeting.mp3")
#bg_sound.play()

while 1:
    pygame.display.update()

    clock.tick(FPS)
    #texts("Hellohellohellohello")
    if player_x1 < 760:
        sc.blit(bg[0], (0, 0))
        #sc.blit(text, text.get_rect(center = sc.get_rect().center))
        #pygame.display.flip()
        #text_rect = ft_font.get_rect('Hello World')
        #text_rect.center = sc.get_rect().center
        #ft_font.render_to(sc, text_rect.topleft, 'Hello World', (255, 0, 0))
        #pygame.display.flip()
    elif player_x1 == 760 and keys[pygame.K_LEFT]:
        sc.blit(bg[0], (0, 0))
        player_x = 759
    elif player_x1 == 760 and keys[pygame.K_RIGHT]:
        sc.blit(bg[1], (0, 0))
        player_x = 0
    elif (player_x1 > 760) and (player_x1 < 760*2):
        #if player_x == 520:
            #player_x = 0
        sc.blit(bg[1], (0, 0))
    elif player_x1 == 760*2 and keys[pygame.K_LEFT]:
        sc.blit(bg[1], (0, 0))
        player_x = 759
    elif player_x1 == 760*2 and keys[pygame.K_RIGHT]:
        sc.blit(bg[2], (0, 0))
        player_x = 0
    elif (player_x1 > 760*2) and (player_x1 < 760*3):
        sc.blit(bg[2], (0, 0))
    elif player_x1 == 760*3 and keys[pygame.K_LEFT]:
        sc.blit(bg[2], (0, 0))
        player_x = 759
    elif player_x1 == 760*3 and keys[pygame.K_RIGHT]:
        sc.blit(bg[3], (0, 0))
        player_x = 0
    elif (player_x1 > 760*3) and (player_x1 < 760*4):
        sc.blit(bg[3], (0, 0))
    elif player_x1 == 760*4 and keys[pygame.K_LEFT]:
        sc.blit(bg[3], (0, 0))
        player_x = 759
    elif player_x1 == 760*4 and keys[pygame.K_RIGHT]:
        sc.blit(bg[4], (0, 0))
        player_x = 0
    elif (player_x1 > 760*4) and (player_x1 < 760*5):
        sc.blit(bg[4], (0, 0))
    elif player_x1 == 760*5 and keys[pygame.K_LEFT]:
        sc.blit(bg[4], (0, 0))
        player_x = 759
    elif player_x1 == 760*5 and keys[pygame.K_RIGHT]:
        sc.blit(bg[5], (0, 0))
        player_x = 0
    elif (player_x1 > 760*5) and (player_x1 < 760*6):
        sc.blit(bg[5], (0, 0))
    #elif (player_x1 == 520*6):
     #   player_x = 519



    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sc.blit(player_right, (player_x, 420))
    elif keys[pygame.K_LEFT]:
        sc.blit(player_left, (player_x, 420))
    #elif (player_x1 > 70) and (player_x1 < 330) and keys[pygame.K_SPACE]:
     #   sc.blit(player_back, (player_x, 420))
      #  sc.blit(dweller1, (300, 390))
    else:
        sc.blit(player_front, (player_x, 420))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if (i.key == pygame.K_SPACE) and (space == 0):
                space = 1
        #           sc.blit(player_back, (player_x, 420))
         #           sc.blit(dweller1, (300, 335))
            elif (i.key == pygame.K_SPACE) and (space == 1):
                space = 2
            elif (i.key == pygame.K_SPACE) and (space == 2):
                space = 3
            elif (i.key == pygame.K_SPACE) and (space == 3):
                space = 0

    if space != 0:
        if (player_x1 > 70) and (player_x1 < 330):
            sc.blit(dweller1, (300, 390))
            sc.blit(player_back, (player_x, 420))
            if space == 2:
                pygame.draw.rect(sc, BEIGE, (player_x - 115, 390, 165, 40))
                draw_text("good afternoon!", text_font, (0, 0, 0), player_x - 100, 395)
            elif space == 3:
                pygame.draw.rect(sc, BEIGE, (350, 370, 195, 40))
                draw_text("what on Earth are you doing", text_font, (0, 0, 0), 355, 375)
                draw_text("here, sweetheart?", text_font, (0, 0, 0), 355, 388)
        elif (player_x1 > 480) and (player_x1 < 700):
            sc.blit(dweller2, (710, 400))
            sc.blit(player_back, (player_x, 420))




    if keys[pygame.K_LEFT] and player_x1 > 0:
        player_x -= player_speed
        player_x1 -= player_speed
    elif keys[pygame.K_RIGHT] and player_x1 < 760*6:
        player_x += player_speed
        player_x1 += player_speed

    if (player_x == 760) and (player_x1 != 760*6):
        if keys[pygame.K_RIGHT]:
            player_x = 0
        elif keys[pygame.K_LEFT]:
            sc.blit(player_left, (759, 420))


    pygame.display.update()





