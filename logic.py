import sys
import pygame
import entity

class logic:
    stateinfo = {

    }
    entities = []

    animations = []

    def __init__(self):
        self.stateinfo["state"] = "combat"
        self.stateinfo["screen"] = (10,10)
        man = entity.entity(0,0,64,64)
        self.entities.append(man)
        self.stateinfo["current_entity"] = self.entities.index(man)
    def resolve_changes(self):
        print("Nothing to do.")

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_entity(self, index):
        return self.entities[index]

    def get_current_entity(self):
        return self.stateinfo["current_entity"]
