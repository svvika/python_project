import pygame
import engine
import random
import math
import json

def prologue(state):
    if not state["initialised"]:
        state["prologue"] = dict()
        char_list = json.loads(open("characters.json","r",encoding="utf-8").read())
        char_no = random.randint(0,3)
        state["progress"] = {
            "character": list(char_list.keys())[char_no],
            "character_location": list(char_list.values())[char_no],
            "insects1" : {"available": False,"attempts": 3,"completed" : False},
            "insects2" : {"available": False,"attempts": 3,"completed" : False},
            "stars1" : {"available": False, "completed" : False},
            "stars2" : {"available": False, "completed" : False},
            "carrots1" : {"available": False, "completed" : False},
            "carrots2" : {"available": False, "completed" : False},
            "mushrooms" : {"available": False, "completed" : False},
            "products" : {"available": False, "completed" : False},
            "water" : {"available": False, "completed" : False},
            "house1" : {"visited": False, "completed" : False},
            "house2" : {"visited": False},
            "house3" : {"visited": False},
            "house4" : {"visited": False},
            "house5" : {"visited": False},
            "house6" : {"visited": False, "completed" : False},
            "house7" : {"visited": False, "completed" : False},
            "house8" : {"visited": False},
            "house9" : {"visited": False},
            "notes" : [False,False,False,False,False,
                       False,False,False,False]
        }
        ps = state["prologue"]
        ps["scene"] = engine.Scene(size=(800, 600),  sprite_named_filenames={"default":"images/prologue_bg.jpg"})
        greeting_text = "Добро пожаловать! Вам нужно найти {0}".format(state["progress"]["character"])
        hint_text = "Движение — стрелками, действие — стрелкой вверх.\nНажмите ВВЕРХ, чтобы начать."
        ps["texts"] = {
            "greeting": engine.Text((0,0),size=36,width=800,text=greeting_text,font_name="advent.ttf"),
            "hint": engine.Text((0,500),size=24,width=800,text=hint_text,font_name="advent.ttf")
        }
        state["initialised"] = True
    ps = state["prologue"]

    if state["k"][pygame.K_UP]:
        state["SWITCH"] = "village"
        del state["prologue"]
    ps["scene"].render(engine.SCREEN)
    for text in ps["texts"].values():
        text.render(engine.SCREEN)
    return state