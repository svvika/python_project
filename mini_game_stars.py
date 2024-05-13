import pygame
import sys
import random


def insertion(ob1, ob2):
    for h1 in ob1.hitbox_list:
        for h2 in ob2.hitbox_list:
            x1, y1, x2, y2 = h1
            x1 += ob1.rect.x
            x2 += ob1.rect.x
            y1 += ob1.rect.y
            y2 += ob1.rect.y
            x3, y3, x4, y4 = h2
            x3 += ob2.rect.x
            x4 += ob2.rect.x
            y3 += ob2.rect.y
            y4 += ob2.rect.y
            if (y2 > y3 and y1 < y4):
                if (x1 < x4 and x2 > x3):
                    return True
    return False

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 50)

class Counter():
    def __init__(self, screen):
        self.screen = screen
        self.cnt = 0

    def plus(self, x):
        self.cnt = max(self.cnt + x, 0)
    def output(self):
        self.screen.blit(my_font.render('Счет: ' + str(self.cnt), False, (255, 255, 255)), (self.screen.get_width() - 300, 20))
class Falling_obj():

    def __init__(self, x, screen):
        self.speed = 0.5
        self.speedup = 0.02
        self.y = 100
        self.screen = screen
        self.image = pygame.image.load("C:\\Users\\User\\Desktop\\Game_for_VSHE\\Sprites\\1.png")
        self.rect = pygame.Rect(x, self.y, 100, 100)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.hitbox_list = [[0, 0, 100, 100]]


    def output(self):
        self.screen.blit(self.image, self.rect)

    def down(self):
        self.y += self.speed
        self.speed += self.speedup
        self.rect.y = int(self.y)

class Bug():

    def __init__(self):
        self.rect = 0
        self.hitbox_list = []


class Player():
    def __init__(self, screen, bug):
        self.speed = 7
        self.screen = screen
        self.w, self.h = pygame.display.get_surface().get_size()
        self.rect = pygame.Rect(0, 0, 350, 550)
        self.rect.y += self.h - self.rect.height + 50
        self.image = pygame.image.load("Sprites\\photo-AmoyShare.png")
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        self.dir = 1

        bug.rect = pygame.Rect(0, 0, self.rect.width * 0.26, self.rect.height * 0.08)
        bug.rect.x = self.rect.x + (self.rect.width * 0.2)
        bug.rect.y = self.rect.y + (self.rect.height * 0.39)
        bug.hitbox_list = [[0, 0, bug.rect.width, bug.rect.height]]
        self.bug = bug

    def output(self):
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, (0, 0, 0), self.bug.rect)

    def move_right(self):
        if (self.rect.x <= self.w - self.rect.width + 50):
            self.rect.x += self.speed
            self.bug_move()
        if (self.dir == 1):
            self.dir = 0
            self.image = pygame.transform.flip(self.image, 1, 0)


    def move_left(self):
        if (self.rect.x >= -50):
            self.rect.x -= self.speed
            self.bug_move()
        if (self.dir == 0):
            self.dir = 1
            self.image = pygame.transform.flip(self.image, 1, 0)

    def bug_move(self):
        if (self.dir == 1):
            self.bug.rect.x = self.rect.x + self.rect.width * 0.2
        if (self.dir == 0):
            self.bug.rect.x = self.rect.x + self.rect.width * 0.53


def run():
    pygame.init()
    screen = pygame.display.set_mode((1900, 1200))

    bug = Bug()
    pl = Player(screen, bug)
    count = Counter(screen)
    tps = 150

    cnt = 0
    l_f_o = []
    bg = pygame.transform.scale(pygame.image.load("Sprites\\night.jpg"), (screen.get_width(), screen.get_height()))


    while True:
        pygame.time.delay(10)
        screen.blit(bg, (0, 0))
        cnt += 1
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            pl.move_right()
        if keys[pygame.K_a]:
            pl.move_left()
        if (cnt % tps) == 0:
            fo = Falling_obj(random.randint(0, screen.get_width() - 100), screen)
            l_f_o.append(fo)
        i = 0
        while i < len(l_f_o):
            obj = l_f_o[i]
            if (insertion(obj, pl.bug)):
                l_f_o.pop(i)
                i -= 1
                count.plus(1)
            elif (obj.rect.y + obj.rect.height >= screen.get_height()):
                l_f_o.pop(i)
                i -= 1
                count.plus(-1)
            i += 1

        for obj in l_f_o:
            obj.down()
            obj.output()

        pl.output()
        count.output()

        pygame.display.update()


run()