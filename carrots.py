import pygame
import sys
import random
import engine




def carrot_fate(state):
    del state["carrots"]["object"]
    state["carrots"]["score"] += 1
    return state

def tile2px(x,y):
    return tuple([x*75 + 100, y*75])

def carrots(state):
    size = (800, 600)
    carrots_time = 85
    player_time = 5
    text_size = 24
    scene_image = "images/carrots_bg.png"
    player_image = "images/player_carrots.png"
    carrot_image = "images/carrot.png"
    text_place = (580, 15)
    tile_size = (75, 75)

    if not state["initialised"]:
        state["carrots"] = dict()
        state["carrots"]["score"] = 0
        state["carrots"]["carrotcooldown"] = 0
        state["carrots"]["movecooldown"] = 0
        state["carrots"]["endtext"] = engine.Text((0,100),size=48, colour="WHITE",text="Вы собрали всю морковь!\nОтнесите её жителю.")
        state["carrots"]["switchcooldown"] = 300
        state["carrots"]["counter"] = engine.Text(text_place, size=text_size, colour="WHITE")
        state["carrots"]["scene"] = engine.Scene(size=size, sprite_named_filenames={"default": scene_image})
        state["carrots"]["player"] = engine.GameEntity((100, 0), tile_size, {"default": player_image})
        state["village"]["music"] = pygame.mixer.music.load("sounds/carrots.mp3")
        pygame.mixer.music.play(-1)
        state["initialised"] = True

    player = state["carrots"]["player"]

    if state["carrots"]["score"] >= 20:
        if state["carrots"]["switchcooldown"] <= 0:
            state["progress"][state["current_task"]]["completed"] = True
            state["progress"][state["current_task"]]["available"] = False
            state["SWITCH"] = "village"
            #state["DO_NOT_REINIT"] = True # позволяет деревне загрузиться такой, как она была; убрать если ломается
            del state["carrots"]
        else:
            state["carrots"]["switchcooldown"] -= 1
            state["carrots"]["endtext"].render(engine.SCREEN)
        return state

    if state["carrots"]["movecooldown"] <= 0:
        state["carrots"]["movecooldown"] = player_time
        if state["k"][pygame.K_RIGHT]:
            if player.pos[0] <= 550:
                player.pos = (player.pos[0]+75,player.pos[1])
        elif state["k"][pygame.K_LEFT]:
            if player.pos[0] >= 175:
                player.pos = (player.pos[0]-75,player.pos[1])

        elif state["k"][pygame.K_UP]:
            if player.pos[1] >= 75:
                player.pos = (player.pos[0],player.pos[1]-75)
        elif state["k"][pygame.K_DOWN]:
            if player.pos[1] <= 450:
                player.pos = (player.pos[0],player.pos[1]+75)
    else:
        state["carrots"]["movecooldown"] -= 1

    if state["carrots"]["carrotcooldown"] <= 0:
        state["carrots"]["carrotcooldown"] = carrots_time
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if "object" in state["carrots"]:
            state["carrots"]["score"] = max(state["carrots"]["score"]-1,0)
        state["carrots"]["object"] = engine.Trigger(tile2px(x,y), tile_size, {"default":carrot_image},
                                                func=carrot_fate,type={"collides"})
  
        #score = max(state["carrots"]["score"]-1,0)
    else:
        state["carrots"]["carrotcooldown"] -= 1



    state["carrots"]["scene"].render(engine.SCREEN)
    if "object" in state["carrots"]:
        state["carrots"]["object"].render(engine.SCREEN)
        state = state["carrots"]["object"].check(state,player)
    player.render(engine.SCREEN)
    state["carrots"]["counter"].text = "Собрано: " + str(state["carrots"]["score"])
    state["carrots"]["counter"].render(engine.SCREEN)

    return state