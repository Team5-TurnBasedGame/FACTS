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
        self.stateinfo["turn"] = "player"
        self.stateinfo["screen"] = (10,10)
        man = entity.entity(0,0,64,64)
        self.entities.append(man)
        self.stateinfo["current_entity"] = self.entities.index(man)

    def resolve_changes(self):
        if self.stateinfo["state"] == "combat"
            if self.stateinfo["turn"] == "player":
                break # nothing to do
            elif self.stateinfo["turn"] == "enemy":
                for entity in self.entities:
                    entity.ai.take_turn()

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_entity(self, index):
        return self.entities[index]

    def get_current_entity(self):
        return self.stateinfo["current_entity"]
