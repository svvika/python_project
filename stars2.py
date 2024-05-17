import pygame
import engine
import random
import math


def star_fate(state, star_name, destination):
    state["stars"]["deathrow"].append(star_name)
    if destination == "basket":
        state["stars"]["score"] += 1
        state["stars"]["starcount"] -= 1
        print(star_name + " collected!", state["stars"]["score"])
    else:
        state["stars"]["score"] = max(state["stars"]["score"] - 1, 0)
        state["stars"]["starcount"] -= 1
        print(star_name + " missed!", state["stars"]["score"])
    return state


def stars(state):
    cooldown = 150
    if not state["initialised"]:
        state["stars"] = dict()
        state["stars"]["score"] = 0
        state["stars"]["starcount"] = 0
        state["stars"]["starcooldown"] = cooldown
        state["stars"]["counter"] = engine.Text(size=16, colour="WHITE")
        state["stars"]["end_of_game_text"] = engine.Text(size=70, colour="WHITE")
        state["stars"]["entities"] = dict()
        state["stars"]["deathrow"] = []
        state["stars"]["triggers"] = dict()
        state["progress"] = dict()
        state["stars"]["cnt"] = 0
        state["progress"]["stars2"] = {"available": False, "completed": False}
        state["progress"]["stars1"] = {"available": False, "completed": False}
        state["stars"]["triggers"]["floor"] = engine.Trigger((0, 600), (800, 1))
        state["stars"]["scene"] = engine.Scene(size=(800, 600), sprite_named_filenames={"default": "images/night.jpg"})
        state["stars"]["entities"]["player"] = engine.GameEntity((57, 442), (96, 250),
                                                                 {"default": "images/player_stars.png", \
                                                                  "right": "images/player_stars_right.png"})
        player = state["stars"]["entities"]["player"]
        state["stars"]["triggers"]["basket"] = engine.Trigger( \
            (player.pos[0] + player.size[0] // 3, player.pos[1]), (player.size[0] // 2, 16))
        state["initialised"] = True

    player = state["stars"]["entities"]["player"]
    basket = state["stars"]["triggers"]["basket"]
    floor = state["stars"]["triggers"]["floor"]

    if state["stars"]["cnt"] == 0:
        if state["stars"]["starcooldown"] == 0:
            state["stars"]["starcount"] += 1
            state["stars"]["starcooldown"] = cooldown
            star = engine.Trigger((random.randint(0, state["stars"]["scene"].size[0] - 64), -80), (64, 64), \
                                  {"default": "images/star.png"}, func=star_fate, type={"collides"})
            star.data["speedy"] = 1
            state["stars"]["entities"]["star" + str(star.id)] = star
        else:
            state["stars"]["starcooldown"] -= 1

    for entity_name in state["stars"]["entities"]:
        if entity_name[:3] == "sta":
            star = state["stars"]["entities"][entity_name]
            star.pos = (star.pos[0], star.pos[1] + star.data["speedy"])
            star.data["speedy"] += 0.05
            state = star.check(state, basket, [entity_name, "basket"])
            state = star.check(state, floor, [entity_name, "floor"])
    for entity_name in state["stars"]["deathrow"]:
        try:
            del state["stars"]["entities"][entity_name]
        except:
            pass
    if state["k"][pygame.K_RIGHT] and player.pos[0] < state["stars"]["scene"].size[0] - 6 - player.size[0]:
        player.current_sprite = "right"
        player.pos = (player.pos[0] + 6, player.pos[1])
    elif state["k"][pygame.K_LEFT]and player.pos[0] > 6:
        player.current_sprite = "default"
        player.pos = (player.pos[0] - 6, player.pos[1])
    elif state["stars"]["cnt"] > 200 and state["k"][pygame.K_DOWN]:
        state["SWITCH"] = "village"

    if player.current_sprite == "default":
        basket.pos = (player.pos[0], player.pos[1] + player.size[1] // 3)
    else:
        basket.pos = (player.pos[0] + player.size[0] // 2, player.pos[1] + player.size[1] // 3)

    state["stars"]["scene"].render(engine.SCREEN)
    # basket.render(engine.SCREEN)
    for entity in state["stars"]["entities"]:
        state["stars"]["entities"][entity].render(engine.SCREEN)
    state["stars"]["counter"].text = "Собрано: " + str(state["stars"]["score"])
    if state["stars"]["score"] >= 25 or state["stars"]["cnt"] > 0:
        state["stars"]["end_of_game_text"].text = "Задание выполнено!\nВсе звезды собраны!\n\nДля выхода нажмите\nстрелку вниз."
        state["stars"]["end_of_game_text"].render(engine.SCREEN)
        if state["progress"]["stars1"]["completed"]:
            state["progress"]["stars2"] = {"available": False, "completed": True}
        else:
            state["progress"]["stars1"] = {"available": False, "completed": True}
        state["stars"]["cnt"] += 1
    state["stars"]["counter"].render(engine.SCREEN)
    return state