import pygame
import engine
import random
import math

def fly_fate(state,fly_name,cloud_name=False):
    if not cloud_name:
        state["insects"]["lives"] -= 1
        state["insects"]["flycount"] -= 1
        state["insects"]["deathrow"].append(fly_name)
        print(state["insects"]["lives"])
        print(fly_name + " dead!")
    else:
        state["insects"]["flycount"] -= 1
        state["insects"]["score"] += 1
        state["insects"]["deathrow"].append(fly_name)
        state["insects"]["deathrow"].append(cloud_name)
        print(fly_name + " dead, as well as " + cloud_name)

    return state

def insects(state):
    if not state["initialised"]:
        state["insects"] = dict()
        state["insects"]["deathrow"] = []
        state["insects"]["flycount"] = 0
        state["insects"]["flycooldown"] = 70
        state["insects"]["guncooldown"] = 0
        state["insects"]["score"] = 0
        state["insects"]["entities"] = dict()
        state["insects"]["entities"] = dict()
        state["insects"]["lives"] = 5
        state["insects"]["scene"] = engine.Scene(size=(800,600),sprite_named_filenames={"default":"images/insects_bg.jpg"})
        state["insects"]["entities"]["player"] = engine.GameEntity((350,500),(51,146),{"default":"images/gun2.png"})
        state["insects"]['counter'] = engine.Text((0,400),size=40,colour = "RED")

        state["initialised"] = True

    if state["insects"]["flycount"] < 8:
        if state["insects"]["flycooldown"] == 0:
            state["insects"]["flycount"] += 1
            state["insects"]["flycooldown"] = 70
            fly = engine.Trigger((random.randint(0,5)*160,-80),(64,64),{"default":"images/bug.png"},func=fly_fate,type={"collides"})
            fly.data["speedx"] = (400 - fly.pos[0])/600
            fly.data["speedy"] = (600 - fly.pos[1])/600
            fly.rot = (math.atan(fly.data["speedx"]/fly.data["speedy"])*180)/3.14
            state["insects"]["entities"]["fly"+str(fly.id)] = fly
        else:
            state["insects"]["flycooldown"] -= 1

    for entity_name in state["insects"]["entities"]:
        if entity_name[:3] == "fly":
            fly = state["insects"]["entities"][entity_name]
            fly.pos = (fly.pos[0]+fly.data["speedx"],fly.pos[1]+fly.data["speedy"])
            state = fly.check(state,state["insects"]["entities"]["player"],params=[entity_name])
            for entity_name_in in state["insects"]["entities"]:
                if entity_name_in[:3] == "clo":
                    state = fly.check(state,state["insects"]["entities"][entity_name_in],params=[entity_name,entity_name_in])
        elif entity_name[:3] == "clo":
            cloud = state["insects"]["entities"][entity_name]
            cloud.pos = (cloud.pos[0]+cloud.data["speedx"],cloud.pos[1]+cloud.data["speedy"])


    for entity_name in state["insects"]["deathrow"]:
        try:
            del state["insects"]["entities"][entity_name]
        except:
            print("I tried")
    state["insects"]["deathrow"] = []

    if state["k"][pygame.K_LEFT]:
        state["insects"]["entities"]["player"].rot -= 5
    elif state["k"][pygame.K_RIGHT]:
        state["insects"]["entities"]["player"].rot += 5
    elif state["k"][pygame.K_UP] and state["insects"]["guncooldown"] < 0:
        state["insects"]["guncooldown"] = 30
        ppos = state["insects"]["entities"]["player"].pos
        cloud = engine.GameEntity((ppos[0]+12,ppos[1]),(64,64),{"default":"images/cloud.png"})
        cloud.data["speedx"] = -math.sin(math.radians(state["insects"]["entities"]["player"].rot))*10
        cloud.data["speedy"] = -math.cos(math.radians(state["insects"]["entities"]["player"].rot))*10
        state["insects"]["entities"]["cloud"+str(cloud.id)] = cloud
    state["insects"]["guncooldown"] -= 1
    if state["insects"]["lives"] == 0:
        state["SWITCH"] = "village"

    state["insects"]["scene"].render(engine.SCREEN)
    state["insects"]["counter"].text = "Жизней: " + str(state["insects"]["lives"]) + "\nУбито: " + str(state["insects"]["score"])
    state["insects"]['counter'].render(engine.SCREEN)
    for entity in state["insects"]["entities"]:
        state["insects"]["entities"][entity].render(engine.SCREEN)

    
    return state