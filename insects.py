import pygame
import engine
import random
import math

def fly_fate(state, fly_name, cloud_name=False):
    if not cloud_name:
        state["insects"]["lives"] -= 1
        state["insects"]["flycount"] -= 1
        state["insects"]["deathrow"].append(fly_name)
        print(state["insects"]["lives"])
        print(fly_name + " dead!")
    else:
        state["insects"]["flycount"] -= 1
        state["insects"]["score"] -= 1
        state["insects"]["deathrow"].append(fly_name)
        state["insects"]["deathrow"].append(cloud_name)
        print(fly_name + " dead, as well as " + cloud_name)

    return state

def insects(state):
    if not state["initialised"]:
        state["insects"] = dict()
        state["insects"]["deathrow"] = []
        state["insects"]["flycount"] = 0
        state["insects"]["flycooldown"] = 60
        state["insects"]["guncooldown"] = 50
        state["insects"]["score"] = 40
        state["insects"]["entities"] = dict()
        state["insects"]["lives"] = 5
        state["insects"]["scene"] = engine.Scene(size=(800, 600),  sprite_named_filenames={"default":"images/insects_bg.jpg",
                                                                                          "end":"images/insects_bg_end.jpg"})
        state["insects"]["entities"]["player"] = engine.GameEntity((375, 450), (51, 146), {"default":"images/gun2.png"})
        state["insects"]["counter"] = engine.Text((10, 450), size=40, colour = "RED")
        state["insects"]["switchdelay"] = 360
        state["insects"]["end_text"] = engine.Text((40, 240), size=40, colour = "RED")

        state["initialised"] = True

    if state["insects"]["lives"] <= 0 or state["insects"]["score"] <= 0:
        print("GO")
        state["insects"]["scene"].current_sprite = "end"
        if state["insects"]["lives"] <= 0:
            state["insects"]["end_text"].text = "Вы не справились с заданием жителя" + "\nУ вас осталось " + str(3) + " попытки"
            state["progress"]["insects"]["attempts"] -= 1
            if state["progress"]["insects"]["attempts"] <= 0:
                state["progress"]["insects"] = {"available":False, "completed":False}

        else:
            state["insects"]["end_text"].text = "Вы справились с заданием жителя" + "\nЗаписка получена!"
            state["progress"]["insects"] = {"available":False, "completed":True}
        if state["insects"]["switchdelay"] <= 0:
            del state["insects"] # нам больше не нужно текущее состояние этой миниигры
            state["SWITCH"] = "village"
        else:
            state["insects"]["switchdelay"] -= 1
            state["insects"]["scene"].render(engine.SCREEN)
            state["insects"]["end_text"].render(engine.SCREEN)
        return state

    if state["insects"]["flycount"] < 9:
        if state["insects"]["flycooldown"] == 0:
            state["insects"]["flycount"] += 1
            state["insects"]["flycooldown"] = 30
            fly = engine.Trigger((random.randint(0, 5)*150, -60), (64, 64),\
            {"default":"images/bug.png"}, func=fly_fate, type={"collides"})
            fly.data["speedx"] = (350 - fly.pos[0])/350
            fly.data["speedy"] = (500 - fly.pos[1])/350
            fly.rot = (math.atan(fly.data["speedx"]/fly.data["speedy"])*180)/3.14
            state["insects"]["entities"]["fly"+str(fly.id)] = fly
        else:
            state["insects"]["flycooldown"] -= 1

    for entity_name in state["insects"]["entities"]:
        if entity_name[:3] == "fly":
            fly = state["insects"]["entities"][entity_name]
            fly.pos = (fly.pos[0]+fly.data["speedx"], fly.pos[1]+fly.data["speedy"])
            state = fly.check(state, state["insects"]["entities"]["player"], params=[entity_name])

            for entity_name_in in state["insects"]["entities"]:
                if entity_name_in[:3] == "clo":
                    state = fly.check(state, state["insects"]["entities"][entity_name_in], params=[entity_name, entity_name_in])
        elif entity_name[:3] == "clo":
            cloud = state["insects"]["entities"][entity_name]
            cloud.pos = (cloud.pos[0]+cloud.data["speedx"], cloud.pos[1]+cloud.data["speedy"])


    for entity_name in state["insects"]["deathrow"]:
        try:
            del state["insects"]["entities"][entity_name]
        except:
            print("I tried")
    state["insects"]["deathrow"] = []

    if state["k"][pygame.K_LEFT]:
        state["insects"]["entities"]["player"].rot += 2
    elif state["k"][pygame.K_RIGHT]:
        state["insects"]["entities"]["player"].rot -= 2

    if state["insects"]["guncooldown"] < 0:
        if state["k"][pygame.K_UP]: # должно исправить проблему с удержанием
            state["insects"]["guncooldown"] = 30
            ppos = state["insects"]["entities"]["player"].pos
            cloud = engine.GameEntity((ppos[0]+12, ppos[1]), (64, 64), {"default":"images/cloud.png"})
            cloud.data["speedx"] = -math.sin(math.radians(state["insects"]["entities"]["player"].rot))*10
            cloud.data["speedy"] = -math.cos(math.radians(state["insects"]["entities"]["player"].rot))*10
            state["insects"]["entities"]["cloud"+str(cloud.id)] = cloud
    else:
        state["insects"]["guncooldown"] -= 1

    state["insects"]["scene"].render(engine.SCREEN)
    state["insects"]['counter'].render(engine.SCREEN)
    for entity in state["insects"]["entities"]:
        state["insects"]["entities"][entity].render(engine.SCREEN)
    state["insects"]["counter"].text = "Жизней: " + str(state["insects"]["lives"]) + "\nОсталось мух: " + str(state["insects"]["score"])
    return state
