import sys
import pygame
import entity

class logic:
    stateinfo = {

    }
    entities = []

    def __init__(self):
        stateinfo["state"] = "combat"
        stateinfo["current_entity"] = "player"

    def resolve_changes(self):
        print()

    def move(self, entity, offset_x, offset_y):
        entity.move(offset_x, offset_y)
