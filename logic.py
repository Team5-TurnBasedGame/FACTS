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
        self.current_entity = None
        self.r = renderer.Renderer(self.screen)

    def resolve_changes(self):
        print()

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_entity(self, index):
        return self.entities[index]

    def get_current_entity(self):
        return self.current_entity

    def play_next_animation(self):
        try:
            currentAnim, currentEntity = tuple(self.animations.pop())
            self.r.animate(currentAnim, currentEntity)
        except: print("No animations.")

class title(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_title_events(self, eventList)

    def render(self):
        self.r.renderBackground()
        self.r.renderTitleScreen()
        pygame.display.flip()

    def cleanUp(self):
        print("Cleaning up title")

class levelSelect(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_level_events(self, eventList)

    def render(self):
        self.r.renderBackground()
        self.r.render_entities(self.entities)
        self.play_next_animation()
        #self.r.renderLevelSelect()
        pygame.display.flip()

    def cleanUp(self):
        print("Cleaning up levelSelect")

class rosterMenu(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_roster_events(self, eventList)

    def render(self):
        print("nothing to render")
        
    def cleanUp(self):
            print("Cleaning up rosterMenu")

    
stateinfo = {
    'title': title(),
    'turn': levelSelect(),
    'roster': rosterMenu()
}
    
def updateState(State):
    if State.done == True:
        if State.next != None:
            temp = stateinfo[State.next]
            State.next = None
            State.done = False
            State.cleanUp()
            return temp
    else:
        return State
    
            
            
