import engine
import pygame
import json

class House():
    def __init__(self,name,dweller,dialogues:list=[]):
        self.visit_times = 0
        self.name = name
        self.dweller = dweller
        self.dialogues = dialogues
        self.note = int(name[-1:])
        #self.dweller.pos = (self.trigger.pos[0]+self.trigger.size[0]-40,self.trigger.pos[1]+self.trigger.size[1])
    def sequence(self,state):
        state["entities"]["player"].current_sprite = "back"
        state["entities"]["dweller"+str(self.note)] = self.dweller
        self.visit_times += 1
        return state
    def render(self,screen):
        pass
    
def village(state):
    if not state["initialised"]:
        state["entities"] = dict()
        state["triggers"] = dict()
        state["entities"]["player"] = engine.GameEntity((57,442),(32,120),
                                    {"default": "images/player_left.png",
                                    "left2": "images/player_left2.png",
                                    "right": "images/player_right.png",
                                    "right2": "images/player_right2.png",
                                    "front": "images/player_front.png",
                                    "back":"images/player_back.png"
                                    })
        state["scene"] = engine.Scene(size=(800,600),sprite_named_filenames=\
                                    {"slide1": "images/slide1.jpg",
                                     "slide2": "images/slide2.jpg",
                                     "slide3": "images/slide3.jpg",
                                     "slide4": "images/slide4.jpg",
                                     "slide5": "images/slide5.jpg",
                                     "slide6": "images/slide6.jpg"
                                     })

        coords_list = json.loads(open("coordinates.json","r").read())
        for house_no in range(1,10):
            house_name = "house"+str(house_no)
            pos = (coords_list[house_name][0],coords_list[house_name][1])
            size = (coords_list[house_name][2],coords_list[house_name][3])
            state["entities"][house_name] = House(house_name,\
                engine.GameEntity((pos[0]+size[0]-30,pos[1]+size[1])))
            state["triggers"][house_name] = engine.Trigger(pos, size,\
                func=state["entities"][house_name].sequence,type=["collides","key"])
        state["slide_no"] = 1
        state["initialised"] = True

    if state["k"][pygame.K_RIGHT]:
        state["entities"]["player"].pos = state["entities"]["player"].pos[0] \
                                    + 3, state["entities"]["player"].pos[1]
        state["entities"]["player"].current_sprite = "right" if\
                        (pygame.time.get_ticks() % 1000 < 500) else "right2"
    elif state["k"][pygame.K_LEFT]:
        state["entities"]["player"].pos = state["entities"]["player"].pos[0] \
                                    - 3, state["entities"]["player"].pos[1]
        state["entities"]["player"].current_sprite = "default" if\
                        (pygame.time.get_ticks() % 1000 < 500) else "left2"
    #elif state["k"][pygame.K_DOWN]:
    #    state["entities"]["player"].current_sprite = "front"
        
    if state["entities"]["player"].pos[0] > 780:
        if state["slide_no"] < 6:
            state["slide_no"] += 1
            state["scene"].current_sprite = "slide" + str(state["slide_no"])
            state["entities"]["player"].pos = (20,state["entities"]["player"].pos[1])
        else:
            state["entities"]["player"].pos = (780,state["entities"]["player"].pos[1])
    
    if state["entities"]["player"].pos[0] < 20:
        if state["slide_no"] > 1:
            state["slide_no"] -= 1
            state["scene"].current_sprite = "slide" + str(state["slide_no"])
            state["entities"]["player"].pos = (780,state["entities"]["player"].pos[1])
        else:
            state["entities"]["player"].pos = (20,state["entities"]["player"].pos[1])

    #if state["triggers"]["house1"].collides(state["entities"]["player"]) and state["k"][pygame.K_UP]:
    #    state["entities"]["player"].current_sprite = "back"

    state["scene"].render(engine.SCREEN)

    for trigger in state["triggers"].values():
        state = trigger.check(state)

    for entity in state["entities"].values():
        entity.render(engine.SCREEN)

    return state