import pygame
import sys

FPS = 60
WIDTH = 800  
HEIGHT = 400
WHITE = (255, 255, 255)
ERROR_IMAGE = pygame.image.load("error.png")

class GameEntity():
    def __init__(self,pos: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"}):
        self.pos = pos
        self.sprites = dict()
        if sprite_named_filenames:
            for sprite_name in sprite_named_filenames.keys():
                self.sprites[sprite_name] = pygame.image.load(sprite_named_filenames[sprite_name])
        self.current_sprite = "default"
    def render(self,screen):
        #TODO: масштабирование
        screen.blit(self.sprites[self.current_sprite],self.pos)

class Scene():
    def __init__(self,image_offset: tuple=(0,0),backround_image_named_filenames: dict = {"default":"error.png"}):
        self.image_offset = image_offset
        self.background_images = dict()
        for bg_name in backround_image_named_filenames:
            try:
                self.background_images[bg_name] = pygame.image.load(backround_image_named_filenames[bg_name])
            except:
                self.background_images[bg_name] = ERROR_IMAGE
        self.current_background_image = "default"
    def render(self,screen):
        #TODO: масштабирование
        screen.blit(self.background_images[self.current_background_image],self.image_offset)

def init():
    global SCREEN
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
    global clock
    clock = pygame.time.Clock()
    pygame.init()

def run(entry_minigame):
    game_running = True
    minigame_state = dict()
    while game_running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        minigame_state["k"] = pygame.key.get_pressed()
        minigame_state = entry_minigame(minigame_state)
        pygame.display.update()
        clock.tick(FPS)