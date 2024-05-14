import pygame
import sys
#from Player import Player
#from Falling_obj import Falling_obj
#from Fly import Fly
import random
#from counter import Counter
#from settings import GameSettings

class GameSettings:
    SCREEN_SIZE = (800, 600)
    BUG_QUANTITY = 50
    GUN_WIDTH = 120
    GUN_HEIGHT = 180
    GUN_DELAY = 50
    FLY_SPEED = 200
    FLY_WIDTH = 80
    FLY_HEIGHT = 80
    FLY_ROTATE = 10
    FALLING_SPEED = 350
    FALLING_WIDTH = 60
    FALLING_HEIGHT = 60

pygame.font.init()
my_font = pygame.font.SysFont('arial', 40)

class Counter():
    def __init__(self, screen):
        self.screen = screen
        self.cnt = 0
        self.lives = 5
        self.bugs = 40

    def plus(self, x):
        self.cnt = max(self.cnt + x, 0)
    def fail(self):
        self.lives = max(0, self.lives - 1)
        if self.lives == 0:
            return True
        else:
            return False

    def output(self):
        self.screen.blit(my_font.render('Жизни: ' + str(self.lives), False, (255, 0, 0)), (30, self.screen.get_height() - 60))
        self.screen.blit(my_font.render('Насекомые: ' + str(self.bugs), False, (255, 0, 0)), (30, self.screen.get_height() - 110))

    def newbug(self):
        self.bugs = max(self.bugs - 1, 0)

    def win(self):
        image = my_font.render('Вы выполнили задание жителя',   False, (255, 0, 0))
        image_2 = my_font.render('Записка получена!', False, (255, 0, 0))
        rect = image.get_rect()
        rect.centery = self.screen.get_height() / 2 - rect.height
        self.screen.blit(image, (100, rect.centery))
        self.screen.blit(image_2, (200, rect.centery + 50))
    def fail_2(self):
        image = my_font.render('Вы не справились с заданием жителя',   False, (255, 0, 0))
        image_2 = my_font.render('У вас осталось 2 попытки', False, (255, 0, 0))
        rect = image.get_rect()
        rect.centery = self.screen.get_height() / 2 - rect.height
        self.screen.blit(image, (50, rect.centery))
        self.screen.blit(image_2, (150, rect.centery + 50))

class Falling_obj:

    def __init__(self, x, screen, number):
        self.speed = GameSettings.FALLING_SPEED
        self.screen = screen
        self.wf = GameSettings.FALLING_WIDTH
        self.hf = GameSettings.FALLING_HEIGHT
        self.image = pygame.image.load("bug.png")
        self.image = pygame.transform.scale(self.image, (self.wf, self.hf))
        angle = 180 + (3 - number) * 15
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.wf / 2
        self.stepx = x - screen.get_rect().centerx
        self.stepy = screen.get_height() - GameSettings.GUN_HEIGHT - 10
        self.step = 0
        self.x0 = x
        self.number = number

    def output(self):
        self.screen.blit(self.image, self.rect)

    def down(self):
        self.step += 1
        self.rect.centery = self.stepy / self.speed * self.step
        self.rect.centerx = self.x0 - self.stepx / self.speed * self.step;

class Fly:
    def __init__(self, x, screen, number):
        self.speed = GameSettings.FLY_SPEED
        self.screen = screen
        self.wf = GameSettings.FLY_WIDTH
        self.hf = GameSettings.FLY_HEIGHT
        self.image = pygame.image.load("ball2.png")
        self.image = pygame.transform.scale(self.image, (self.wf, self.hf))
        self.rect = self.image.get_rect()

        self.stepx = x
        self.stepy = screen.get_height() - GameSettings.GUN_HEIGHT
        self.step = 0
        self.x0 = screen.get_rect().centerx + (number - 3) * 50
        self.y0 = screen.get_height() - GameSettings.GUN_HEIGHT - self.hf
        self.rect.centerx = self.x0
        self.rect.centery = self.y0
        self.number = number
        self.angle = 0

    def output(self):
        rotimage = pygame.transform.rotate(self.image, self.angle)
        rotrect = rotimage.get_rect(center=self.rect.center)
        self.screen.blit(rotimage, rotrect)
        #self.angle += GameSettings.FLY_ROTATE
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 8)

    def up(self):
        self.step += 1
        self.rect.centery = self.y0 - self.stepy / self.speed * self.step
        self.rect.centerx = self.x0 - self.stepx / self.speed * self.step

class Player:
    def __init__(self, screen):
        self.speed = 1
        self.cnt = 0
        self.screen = screen
        self.w, _ = pygame.display.get_surface().get_size()
        self.wp = GameSettings.GUN_WIDTH
        self.hp = GameSettings.GUN_HEIGHT
        self.image = pygame.image.load("gun2.png")
        self.orig_image = pygame.transform.scale(self.image, (self.wp, self.hp))
        #
        self.rect = self.orig_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.angle = 0
        self.addangle = 15
        self.newangle = self.angle

        self.origx = self.rect.centerx
        self.origy = self.rect.centery
        self.origmidtop = self.rect.midtop
        self.number = 3

    def output(self):
        self.cnt += 1
        if self.cnt % self.speed == 0:
            if self.newangle > self.angle:
                self.angle += 1
            if self.newangle < self.angle:
                self.angle -= 1
        rotimage = pygame.transform.rotate(self.orig_image, self.angle)
        image_rect = self.orig_image.get_rect()
        rotrect = rotimage.get_rect(center=image_rect.center)
        rotrect.centerx = self.screen_rect.centerx
        rotrect.bottom = self.screen_rect.bottom
        self.screen.blit(rotimage, rotrect)

    def move_right(self):
        if self.angle == self.newangle:
            self.newangle = max(self.angle - self.addangle, -2 * self.addangle)
            self.number = min(self.number + 1, 5)

    def move_left(self):
        if self.angle == self.newangle:
            self.newangle = min(self.angle + self.addangle, 2 * self.addangle)
            self.number = max(self.number - 1, 1)

def run():
    pygame.init()
    screen = pygame.display.set_mode(GameSettings.SCREEN_SIZE)

    pl = Player(screen)
    count = Counter(screen)
    tps = GameSettings.BUG_QUANTITY
    background_image = pygame.image.load("background.jpg")
    background_image = pygame.transform.scale(background_image, (800, 600))

    cnt = 0
    l_f_o = []
    fly_o = []
    blast_o = []
    gundelay = 0

    while True:
        pygame.time.delay(10)
        skyrect = pygame.Rect(0, 0, screen.get_width(), screen.get_height() - 200)  #по иксу 0, по игреку 0 - начало прямоугольника, ширина экрана, высота - 200 - конец прямоугольника
        fieldrect = pygame.Rect(0, screen.get_height() - 200, screen.get_width(), screen.get_height() )
        screen.blit(background_image, (0, 0))

        cnt += 1
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            pl.move_right()
        if keys[pygame.K_LEFT]:
            pl.move_left()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        if keys[pygame.K_UP] and gundelay == 0:
            x = screen.get_width() / 4 * (3 - pl.number)
            fo = Fly(x, screen, pl.number)
            fly_o.append(fo)
            gundelay = GameSettings.GUN_DELAY
        gundelay = max(gundelay - 1, 0)
        if (cnt % tps) == 0:
            q = random.randint(0, 4)
            x = screen.get_width() / 4 * q
            fo = Falling_obj(x, screen, q + 1)
            l_f_o.append(fo)
            count.newbug()

        i = 0
        while i < len(l_f_o):
            obj = l_f_o[i]
            if obj.rect.centery > screen.get_height() - GameSettings.GUN_HEIGHT:
                count.fail()
                l_f_o.pop(i)
            i += 1
        i = 0
        while i < len(fly_o):
            obj = fly_o[i]
            if obj.rect.centery < 0:
                fly_o.pop(i)
            i += 1

        for obj in l_f_o:
            obj.down()
            obj.output()


        pl.output()
        for obj in fly_o:
            obj.up()
            obj.output()

        i = 0
        while i < len(l_f_o):
            obj1 = l_f_o[i]
            j = 0
            while j < len(fly_o):
                obj2 = fly_o[j]
                if obj1.number == obj2.number and obj1.rect.centery > obj2.rect.centery:
                    l_f_o.pop(i)
                    fly_o.pop(j)
                j += 1
            i += 1
        count.output()

        i = 0
        while i < len(blast_o):
            if blast_o[i].lifetime <= 0:
                blast_o.pop(i)
            i += 1

        pygame.display.update()
        if count.lives == 0:
            #sys.exit()
            screen.blit(background_image, (0, 0))
            count.fail_2()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    break
            break
        if count.bugs == 0:
            screen.blit(background_image, (0, 0))
            count.win()
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    break
            break
run()
