import sys
import pygame
import entity
import renderer
import eventhandler as eh

class State:
    
    entities = []
    animations = []

    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
        self.screen = (10,10)
        
        man = entity.entity(0,0,64,64)
        self.entities.append(man)
        self.current_entity = man

    def resolve_changes(self):
        print()

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_entity(self, index):
        return self.entities[index]

    def get_current_entity(self):
        return self.current_entity
    


class title(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_title_events(self, eventList)

    def render(self):
        print("rendering title")

class levelSelect(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_level_events(self, eventList)
    def render(self):
        print("rendering levelSelect")

class rosterMenu(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
            eventList = pygame.event.get()
            eh.handle_system_events(self, eventList)
            eh.handle_roster_events(self, eventList)

    def render(self):
            print("rendering RosterMenu")


    #def __init__(self):
        #self.stateinfo["state"] = "combat"
        #print(self.stateinfo["state"]
        #self.stateinfo["turn"] = "player"
        #
        #man = entity.entity(0,0,64,64)
        #self.entities.append(man)
        #self.stateinfo["current_entity"] = self.entities.index(man)

    
stateinfo = {
    'title': title(),
    'turn': levelSelect(),
    'roster': rosterMenu()
}
    
def updateState(State):
    if State.done == True:
        if State.next != None:
            return stateinfo[State.next]
    else:
        return State
    
            
            
