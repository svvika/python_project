import pygame
import sys
import random

ERROR_IMAGE = pygame.image.load("error.png")
random.seed()

class GameEntity():
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"},rot=0.0):
        self.id = random.randint(1, sys.maxsize)
        print(self.id)
        self.pos = pos
        self.rot = rot
        self.size = size
        self.data = dict()
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
        global global_offset
        screen.blit(
            pygame.transform.rotate(
            pygame.transform.scale(sprite,\
                    tuple([sprite_size[0]*global_scale,\
                        sprite_size[1]*global_scale])),self.rot),\
                    tuple([(self.pos[0]-global_offset[0])*global_scale,(self.pos[1]-global_offset[1])*global_scale])
                    
                    )

class Trigger(GameEntity):
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"},\
                func=lambda x : x,type={},default_params=[],key=pygame.K_UP,cooldown=0,once=True):
        super().__init__(pos,size,sprite_named_filenames)
        self.func = func
        self.once = once
        self.default_params = default_params
        self.type = type
        self.key = key
        self.cooldown = cooldown
        self.last_fired = 0
        self.fired = False
    def collides(self,entity):
        return pygame.Rect(self.pos,self.size).colliderect(pygame.Rect(entity.pos,entity.size))
    def contains(self,entity):
        return pygame.Rect(self.pos,self.size).contains(pygame.Rect(entity.pos,entity.size))
    def check(self,state,target,params=[]):
        if not params:
            params = self.default_params
        check_result = set()
        if self.collides(target):
            check_result.add("collides")
        if state["k"][self.key]:
            check_result.add("key")
        if (check_result == self.type) and (not self.fired) and (pygame.time.get_ticks() - self.last_fired >= self.cooldown):
            if self.once:
                self.fired = True
            self.last_fired = pygame.time.get_ticks()
            return self.func(state,*params)
        else:
            return state

class Scene(GameEntity):
    def __init__(self,pos: tuple=(0,0),size: tuple=(0,0),sprite_named_filenames: dict = {"default":"error.png"}):
        super().__init__(pos,size,sprite_named_filenames)

class Text():
    def load_font(self,font_name,size):
        try:
            font = pygame.font.Font(font_name,self.size)
        except:
            try:
                font = pygame.font.SysFont(font_name,self.size)
            except:
                font = pygame.font.SysFont("Arial",self.size)
        return font
    def __init__(self,pos: tuple=(0,0),size: int = 16,font_name="Arial",text="",colour='WHITE',width=800,box_colour=(0,0,0,0)):
        self.pos = pos
        self.width = width
        self.size = size
        self.render_size = self.size
        self.text = text
        self.colour = colour
        self.font_name = font_name
        self.font = self.load_font(self.font_name,self.size)
        self.box_colour = box_colour
    def render(self,screen):
        global global_scale
        global global_offset

        #if self.render_size != round(self.size*global_scale):
        #    print(self.render_size,round(self.size*global_scale))
        #    self.render_size = round(self.size*global_scale)
        #    self.font = self.load_font(self.font_name,self.render_size)
        accum = ""
        total = ""
        for word in self.text.split(" "):
            if self.font.size(accum+word)[0] <= self.width:
                accum += word + " "
            else:
                total += accum + "\n"
                accum = word + " "
        total += accum
        line_surfaces = []
        line_no = 0
        total_height = 0
        for line in total.split("\n"):
            line_no += 1
            surface = self.font.render(line,True,self.colour)
            line_surfaces.append(surface)
            total_height += surface.get_size()[1]
        box = pygame.Surface((self.width,total_height)).convert_alpha()
        box.fill(self.box_colour)
        line_no = 0
        for line in line_surfaces:
            box.blit(line,(0,line_no*self.size))
            line_no += 1
        box = pygame.transform.scale(box,\
                    tuple([self.width*global_scale,\
                        total_height*global_scale]))
        screen.blit(box,\
        tuple([(self.pos[0]-global_offset[0])*global_scale,(self.pos[1]-global_offset[1])*global_scale]))

def init(m):
    global FPS
    global global_offset
    global window_height
    global global_scale
    global window_width
    global clock
    global minigames
    global SCREEN
    FPS = 60
    window_width = 800  
    window_height = 600
    global_scale = 1
    global_offset = [0,0]
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    SCREEN = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Тайна деревни")
    clock = pygame.time.Clock()
    minigames = m
    pygame.init()

def run(entry_minigame_name):
    global global_scale
    global global_offset
    game_running = True
    fullscreen = False
    fullscreen_last = pygame.time.get_ticks()
    minigame_state = dict()
    minigame_state["SWITCH"] = False
    minigame_state["DO_NOT_REINIT"] = False
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
            print("SW")
            current_minigame = minigames[minigame_state["SWITCH"]]
            global_offset = [0,0]
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            minigame_state["SWITCH"] = False
            minigame_state["initialised"] = minigame_state["DO_NOT_REINIT"]
            minigame_state["DO_NOT_REINIT"] = False
        pygame.display.update()
        clock.tick(FPS)
