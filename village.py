import engine
import pygame

def village(state):
    if not "entities" in state.keys():
        state["entities"] = dict()
        state["entities"]["player"] = engine.GameEntity((0,0),{"default": "images/player_left.png", "left2": "images/player_left2.png","right": "images/player_right.png","right2": "images/player_right2.png"})
    if not "scene" in state.keys():
        state["scene"] = engine.Scene((0,0),{"default": "images/bg0.jpg"})
    if state["k"][pygame.K_RIGHT]:
        state["entities"]["player"].pos = state["entities"]["player"].pos[0] + 1 , state["entities"]["player"].pos[1]
        state["entities"]["player"].current_sprite = "right" if (pygame.time.get_ticks() % 1000 < 500) else "right2"
    elif state["k"][pygame.K_LEFT]:
        state["entities"]["player"].pos = state["entities"]["player"].pos[0] - 1 , state["entities"]["player"].pos[1]
        state["entities"]["player"].current_sprite = "default" if (pygame.time.get_ticks() % 1000 < 500) else "left2"
    state["scene"].render(engine.SCREEN)
    for entity in state["entities"].values():
        entity.render(engine.SCREEN)
    #state["entities"]["player"].pos = state["entities"]["player"].pos[0] + 1 , state["entities"]["player"].pos[1] 
    return state