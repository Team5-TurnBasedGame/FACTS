import sys
import pygame as pg
import entity

class State:
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

class title(State):
        def __init__(self):
            State.__init__(self)

class levelSelect(State):
        def __init__(self):
            State.__init__(self)


class rosterMenu(State):
    def __init__(self):
        State.__init__(self)


    stateinfo = {
            'title': title(),
            'turn': levelSelect(),
            #'roster': rosterMenu()
            
    }
    entities = []

    animations = []

    #def __init__(self):
        #self.stateinfo["state"] = "combat"
        #print(self.stateinfo["state"]
        #self.stateinfo["turn"] = "player"
       # self.stateinfo["screen"] = (10,10)
        #man = entity.entity(0,0,64,64)
        #self.entities.append(man)
        #self.stateinfo["current_entity"] = self.entities.index(man)
class gameLogic:
    def resolve_changes(self):
       # if self.stateinfo["state"] == "combat"
        #    if self.stateinfo["turn"] == "player":
           # elif self.stateinfo["turn"] == "enemy":
            #    for entity in self.entities:
             #       entity.ai.take_turn()
        print()

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_entity(self, index):
        return self.entities[index]

    def get_current_entity(self):
        return self.stateinfo["current_entity"]


              

  
            
