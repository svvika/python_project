import pygame
import engine
import random
import math
import json


def prologue(state):
    if not state["initialised"]:
        state["prologue"] = dict()
        char_list = json.loads(open("characters.json", "r", encoding="utf-8").read())
        char_no = random.randint(0, 3)
        state["progress"] = {
            "character": list(char_list.keys())[char_no],
            "character_location": list(char_list.values())[char_no],
            "insects1": {"available": False, "attempts": 3, "completed": False},
            "insects2": {"available": False, "attempts": 3, "completed": False},
            "stars1": {"available": False, "completed": False},
            "stars2": {"available": False, "completed": False},
            "carrots1": {"available": False, "completed": False},
            "carrots2": {"available": False, "completed": False},
            "mushrooms": {"available": False, "completed": False},
            "products": {"available": False, "completed": False},
            "water": {"available": False, "completed": False},
            "house1": {"visited": False, "completed": False},
            "house2": {"visited": False},
            "house3": {"visited": False},
            "house4": {"visited": False},
            "house5": {"visited": False},
            "house6": {"visited": False, "completed": False},
            "house7": {"visited": False, "completed": False},
            "house8": {"visited": False},
            "house9": {"visited": False},
            "notes": [False, False, False, False, False, False, False, False, False, False]
        }
        ps = state["prologue"]
        ps["scene"] = engine.Scene(size=(800, 600), sprite_named_filenames={"default": "images/prologue_bg.jpg"})
        hello_text = "Добро пожаловать!"
        greeting_text = ("Вы студент-участник экспедиции в деревню, в округе которой, как ходят слухи, обитают лесные "
                         "существа из древнерусской мифологии. Ваша цель - доказать, что существует {0}. Найти этого "
                         "персонажа вам помогут местные жители, готовые рассказать, что знают, за небольшую помощь. "
                         "Искать следует в месте, которое чаще всего упоминается как место этого "
                         "существа. Поговорив со всеми жителями, отправляйся, ни на что не отвлекаясь, на поиски "

                         "нужной локации.").format(state["progress"]["character"])

        goodluck_text = "Удачи!"
        hint_text = "Кнопки:\nХодить: ВПРАВО, ВЛЕВО\nДействие: ВВЕРХ\nВыйти из леса: ВНИЗ\nНайти сущ-во: Enter\nИнвентарь: Tab\nЧитать записку: 0-9\nНажмите ВВЕРХ,\n чтобы играть!"
        switch_text = " "
        text_x = 25
        text_w = 740
        ps["texts"] = {
            "hello": engine.Text((text_x, 60), size=29, width=text_w, text=hello_text, font_name="advent.ttf"),
            "greeting": engine.Text((text_x, 102), size=24, width=text_w, text=greeting_text, font_name="advent.ttf"),
            "goodluck": engine.Text((text_x, 280), size=24, width=text_w, text=goodluck_text, font_name="advent.ttf"),

            "hint": engine.Text((340, 280), size=18, width=800, text=hint_text, font_name="advent.ttf"),

            "switch": engine.Text((7, 578), size=18, width=800, text=switch_text, font_name="advent.ttf")
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
