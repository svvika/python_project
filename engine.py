import pygame
import sys
import random

FPS = 60
window_width = 800  
window_height = 600

ERROR_IMAGE = pygame.image.load("error.png")
random.seed()

class GameEntity():
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"}):
        self.id = random.randint(1, sys.maxsize)
        print(self.id)
        self.pos = pos
        self.size = size
        self.sprites = dict()
        if sprite_named_filenames:
            for sprite_name in sprite_named_filenames.keys():
                try:
                    self.sprites[sprite_name] = pygame.image.load(sprite_named_filenames[sprite_name])
                except:
                    self.sprites[sprite_name] = ERROR_IMAGE
        self.default_sprite = self.sprites[list(sprite_named_filenames.keys())[0]]
        self.current_sprite = self.default_sprite
        if not (size[0] and size[1]):
            self.size = self.default_sprite.get_size()
    def render(self,screen):
        try:
            sprite = self.sprites[self.current_sprite]
        except:
            sprite = self.default_sprite
        sprite_size = self.size
        #print(tuple([sprite_size[0]*global_scale,sprite_size[1]*global_scale]))
        if pygame.time.get_ticks() % 1000 == 0:
            print(global_scale)
        screen.blit(pygame.transform.scale(sprite,tuple([sprite_size[0]*global_scale,sprite_size[1]*global_scale])),self.pos)

class Trigger(GameEntity):
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"}):
        super().__init__(pos,size,sprite_named_filenames)
    def collides(self,entity):
        return pygame.Rect(self.pos,self.size).colliderect(pygame.Rect(entity.pos,entity.size))
    def contains(self,entity):
        return pygame.Rect(self.pos,self.size).contains(pygame.Rect(entity.pos,entity.size))


class Scene(GameEntity):
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"}):
        super().__init__(pos,size,sprite_named_filenames)

def init():
    global SCREEN
    SCREEN = pygame.display.set_mode((window_width, window_height))
    global global_scale
    global_scale = 1
    global clock
    clock = pygame.time.Clock()
    pygame.init()

def run(entry_minigame):
    game_running = True
    fullscreen = False
    fullscreen_last = pygame.time.get_ticks()
    minigame_state = dict()
    while game_running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        minigame_state["k"] = pygame.key.get_pressed()
        if minigame_state["k"][pygame.K_F3] and (pygame.time.get_ticks() - fullscreen_last) > 1000:
            if fullscreen:
                global_scale = 1
                SCREEN = pygame.display.set_mode((window_width, window_height))
            else:
                tw = pygame.display.get_desktop_sizes()[0][0]
                th = pygame.display.get_desktop_sizes()[0][1]
                global_scale = th / 600
                print(global_scale)
                print((th*4//3,th))
                SCREEN = pygame.display.set_mode((th*4//3,th),pygame.FULLSCREEN)
            fullscreen_last = pygame.time.get_ticks()
            fullscreen = not fullscreen
        minigame_state = entry_minigame(minigame_state)
        pygame.display.update()
        clock.tick(FPS)