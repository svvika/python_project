import pygame
import sys
import random

import ogorod_info

pygame.font.init()
text_font = pygame.font.Font(None, 24)


def grid_screen(screen):
    for x in range(0, ogorod_info.WIDTH, ogorod_info.TILE_SIZE):
        pygame.draw.line(screen, ogorod_info.BLACK, (x, 0), (x, ogorod_info.HEIGHT))
    for y in range(0, ogorod_info.HEIGHT, ogorod_info.TILE_SIZE):
        pygame.draw.line(screen, ogorod_info.BLACK, (0, y), (ogorod_info.WIDTH, y))


def make_screen(screen):
    screen.fill(ogorod_info.BROWN)
    grid_screen(screen)


class Counter:
    def __init__(self, screen):
        self.screen = screen
        self.count = 0

    def plus(self, x: int):
        self.count = max(self.count + x, 0)

    def output(self):
        placement = (ogorod_info.WIDTH * 4 // 5, ogorod_info.HEIGHT // 40)
        self.screen.blit(text_font.render("Собрано: " + str(self.count), False, ogorod_info.WHITE), placement)


class Player:
    def __init__(self, screen, x: int, y: int):
        self.screen = screen
        self.image = pygame.image.load(ogorod_info.PLAYER)
        self.image = pygame.transform.scale(self.image, (ogorod_info.TILE_SIZE, ogorod_info.TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * ogorod_info.TILE_SIZE
        self.rect.y = y * ogorod_info.TILE_SIZE
        self.x = x
        self.y = y

    def output(self):
        self.screen.blit(self.image, self.rect)

    def move_right(self):
        if self.rect.right <= ogorod_info.WIDTH - ogorod_info.TILE_SIZE:
            self.rect.x += ogorod_info.TILE_SIZE
            self.x += 1

    def move_left(self):
        if self.rect.left >= ogorod_info.TILE_SIZE:
            self.rect.x -= ogorod_info.TILE_SIZE
            self.x -= 1

    def move_up(self):
        if self.rect.top >= ogorod_info.TILE_SIZE:
            self.rect.y -= ogorod_info.TILE_SIZE
            self.y -= 1

    def move_down(self):
        if self.rect.bottom <= ogorod_info.HEIGHT - ogorod_info.TILE_SIZE:
            self.rect.y += ogorod_info.TILE_SIZE
            self.y += 1


class AppearingObject:
    def __init__(self, screen, x: int, y: int):
        self.screen = screen
        self.image = pygame.image.load(ogorod_info.OBJECT)
        self.image = pygame.transform.scale(self.image, (ogorod_info.TILE_SIZE, ogorod_info.TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x * ogorod_info.TILE_SIZE
        self.rect.y = y * ogorod_info.TILE_SIZE
        self.x = x
        self.y = y

    def output(self):
        self.screen.blit(self.image, self.rect)

    def collide(self, player: Player):
        if player.x == self.x and player.y == self.y:
            return True
        return False


def run():
    pygame.init()
    screen = pygame.display.set_mode(ogorod_info.SCREEN_SIZE)
    clock = pygame.time.Clock()
    player = Player(screen, 0, 0)
    count = Counter(screen)

    loop = True
    timer = 0
    objects = []

    while loop:
        pygame.time.delay(23)
        clock.tick(ogorod_info.FPS)
        timer += 1

        make_screen(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_UP]:
            player.move_up()
        if keys[pygame.K_DOWN]:
            player.move_down()

        if (timer % ogorod_info.TPS) == 0:
            cell_w = random.randint(0, ogorod_info.TILE_NUM_W - 1)
            cell_h = random.randint(0, ogorod_info.TILE_NUM_H - 1)
            if objects:
                count.plus(-1)
                objects = []
            object = AppearingObject(screen, cell_w, cell_h)
            objects.append(object)

        for object in objects:
            object.output()
            i = objects.index(object)
            if object.collide(player):
                count.plus(1)
                objects.pop(i)

        if int(count.count) == ogorod_info.WIN_COUNT:
            break

        player.output()
        count.output()
        pygame.display.update()


run()
