import pygame
import sys
import random

FPS = 60
window_width = 800  
window_height = 600

global_scale = 1

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
        global global_scale
        screen.blit(pygame.transform.scale(sprite,\
                    tuple([sprite_size[0]*global_scale,sprite_size[1]*global_scale])),\
                    tuple([self.pos[0]*global_scale,self.pos[1]*global_scale]))

class Trigger(GameEntity):
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"},\
                func=lambda : 0,type=[]):
        super().__init__(pos,size,sprite_named_filenames)
        self.func = func
        self.type = type
    def collides(self,entity):
        return pygame.Rect(self.pos,self.size).colliderect(pygame.Rect(entity.pos,entity.size))
    def contains(self,entity):
        return pygame.Rect(self.pos,self.size).contains(pygame.Rect(entity.pos,entity.size))
    def check(self,state):
        if ("collides" in self.type and self.collides(state["entities"]["player"])) and\
        ("key" in self.type and state["k"][pygame.K_UP]):
            return self.func(state)
        else:
            return state

class Scene(GameEntity):
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"}):
        super().__init__(pos,size,sprite_named_filenames)

def init(m):
    global SCREEN
    SCREEN = pygame.display.set_mode((window_width, window_height))
    global clock
    clock = pygame.time.Clock()
    global minigames
    minigames = m
    pygame.init()

def run(entry_minigame_name):
    global global_scale
    game_running = True
    fullscreen = False
    fullscreen_last = pygame.time.get_ticks()
    minigame_state = dict()
    minigame_state["SWITCH"] = False
    minigame_state["initialised"] = False
    current_minigame = minigames[entry_minigame_name]
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
                SCREEN = pygame.display.set_mode((th*4//3,th),pygame.FULLSCREEN)
            fullscreen_last = pygame.time.get_ticks()
            fullscreen = not fullscreen
        minigame_state = current_minigame(minigame_state)
        if minigame_state["SWITCH"]:
            current_minigame = minigames[minigame_state["SWITCH"]]
            minigame_state["SWITCH"] = False
            minigame_state["initialised"] = False
        pygame.display.update()
        clock.tick(FPS)