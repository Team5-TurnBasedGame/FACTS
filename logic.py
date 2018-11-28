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
        self.r = renderer.Renderer(self.screen)

    def resolve_changes(self):
        pass

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
        except:
            pass

    def next_entity(self):
        current_index = self.entities.index(self.current_entity)
        if current_index+1 < self.entities.len():
            self.current_entity = self.entities[current_index + 1]
        else:
            self.current_entity = self.entities[0]
        if self.current_entity.hp <= 0:
            self.animations.append(("die", self.current_entity))

class Title(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_title_events(self, eventList)

    def render(self):
        self.r.render_background()
        self.r.renderTitleScreen()
        pygame.display.flip()

    def clean_up(self):
        print("Cleaning up title")

class LevelSelect(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_level_events(self, eventList)

    def render(self):
        self.r.render_background()
        self.r.renderLevelSelect()
        pygame.display.flip()

    def clean_up(self):
        print("Cleaning up levelSelect")

class RosterMenu(State):
    def __init__(self):
        State.__init__(self)

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_roster_events(self, eventList)

    def render(self):
        print("nothing to render")
        
    def clean_up(self):
            print("Cleaning up rosterMenu")

class Combat(State):
    def __init__(self):
        State.__init__(self)

        State.entities.append(self.factory("SwordsMan"))
        State.entities.append(self.factory("ArcherWoman"))
        State.entities.append(self.factory("ElfWoman"))
        State.entities.append(self.factory("SpearsMan"))
        State.entities.append(self.factory("WizardMan"))
        State.current_entity = State.entities[0]

        self.action = None
        
    def factory(self, type):
        if type == "SwordsMan":
            walkRight = [pygame.image.load('media/sprites/SwordsMan/WR/1.png'), pygame.image.load('media/sprites/SwordsMan/WR/2.png'), pygame.image.load('media/sprites/SwordsMan/WR/3.png'), pygame.image.load('media/sprites/SwordsMan/WR/4.png'), pygame.image.load('media/sprites/SwordsMan/WR/5.png'), pygame.image.load('media/sprites/SwordsMan/WR/6.png'), pygame.image.load('media/sprites/SwordsMan/WR/7.png'), pygame.image.load('media/sprites/SwordsMan/WR/8.png'), pygame.image.load('media/sprites/SwordsMan/WR/9.png')]
            walkUp = [pygame.image.load('media/sprites/SwordsMan/WU/1.png'), pygame.image.load('media/sprites/SwordsMan/WU/2.png'), pygame.image.load('media/sprites/SwordsMan/WU/3.png'), pygame.image.load('media/sprites/SwordsMan/WU/4.png'), pygame.image.load('media/sprites/SwordsMan/WU/5.png'), pygame.image.load('media/sprites/SwordsMan/WU/6.png'), pygame.image.load('media/sprites/SwordsMan/WU/7.png'), pygame.image.load('media/sprites/SwordsMan/WU/8.png'), pygame.image.load('media/sprites/SwordsMan/WU/9.png')]
            walkLeft = [pygame.image.load('media/sprites/SwordsMan/WL/1.png'), pygame.image.load('media/sprites/SwordsMan/WL/2.png'), pygame.image.load('media/sprites/SwordsMan/WL/3.png'), pygame.image.load('media/sprites/SwordsMan/WL/4.png'), pygame.image.load('media/sprites/SwordsMan/WL/5.png'), pygame.image.load('media/sprites/SwordsMan/WL/6.png'), pygame.image.load('media/sprites/SwordsMan/WL/7.png'), pygame.image.load('media/sprites/SwordsMan/WL/8.png'), pygame.image.load('media/sprites/SwordsMan/WL/9.png')]
            walkDown = [pygame.image.load('media/sprites/SwordsMan/WD/1.png'), pygame.image.load('media/sprites/SwordsMan/WD/2.png'), pygame.image.load('media/sprites/SwordsMan/WD/3.png'), pygame.image.load('media/sprites/SwordsMan/WD/4.png'), pygame.image.load('media/sprites/SwordsMan/WD/5.png'), pygame.image.load('media/sprites/SwordsMan/WD/6.png'), pygame.image.load('media/sprites/SwordsMan/WD/7.png'), pygame.image.load('media/sprites/SwordsMan/WD/8.png'), pygame.image.load('media/sprites/SwordsMan/WD/9.png')]
            char = pygame.image.load('media/sprites/SwordsMan/char.png')
            standing = pygame.image.load('media/sprites/SwordsMan/char.png')
            return entity.Unit(self, 4, 4, 50, 50, char, standing, walkRight, walkLeft)
        if type == "ArcherWoman":
            walkRight = [pygame.image.load('media/sprites/ArcherWoman/WR/1.png'), pygame.image.load('media/sprites/ArcherWoman/WR/2.png'), pygame.image.load('media/sprites/ArcherWoman/WR/3.png'), pygame.image.load('media/sprites/ArcherWoman/WR/4.png'), pygame.image.load('media/sprites/ArcherWoman/WR/5.png'), pygame.image.load('media/sprites/ArcherWoman/WR/6.png'), pygame.image.load('media/sprites/ArcherWoman/WR/7.png'), pygame.image.load('media/sprites/ArcherWoman/WR/8.png'), pygame.image.load('media/sprites/ArcherWoman/WR/9.png')]
            walkUp = [pygame.image.load('media/sprites/ArcherWoman/WU/1.png'), pygame.image.load('media/sprites/ArcherWoman/WU/2.png'), pygame.image.load('media/sprites/ArcherWoman/WU/3.png'), pygame.image.load('media/sprites/ArcherWoman/WU/4.png'), pygame.image.load('media/sprites/ArcherWoman/WU/5.png'), pygame.image.load('media/sprites/ArcherWoman/WU/6.png'), pygame.image.load('media/sprites/ArcherWoman/WU/7.png'), pygame.image.load('media/sprites/ArcherWoman/WU/8.png'), pygame.image.load('media/sprites/ArcherWoman/WU/9.png')]
            walkLeft = [pygame.image.load('media/sprites/ArcherWoman/WL/1.png'), pygame.image.load('media/sprites/ArcherWoman/WL/2.png'), pygame.image.load('media/sprites/ArcherWoman/WL/3.png'), pygame.image.load('media/sprites/ArcherWoman/WL/4.png'), pygame.image.load('media/sprites/ArcherWoman/WL/5.png'), pygame.image.load('media/sprites/ArcherWoman/WL/6.png'), pygame.image.load('media/sprites/ArcherWoman/WL/7.png'), pygame.image.load('media/sprites/ArcherWoman/WL/8.png'), pygame.image.load('media/sprites/ArcherWoman/WL/9.png')]
            walkDown = [pygame.image.load('media/sprites/ArcherWoman/WD/1.png'), pygame.image.load('media/sprites/ArcherWoman/WD/2.png'), pygame.image.load('media/sprites/ArcherWoman/WD/3.png'), pygame.image.load('media/sprites/ArcherWoman/WD/4.png'), pygame.image.load('media/sprites/ArcherWoman/WD/5.png'), pygame.image.load('media/sprites/ArcherWoman/WD/6.png'), pygame.image.load('media/sprites/ArcherWoman/WD/7.png'), pygame.image.load('media/sprites/ArcherWoman/WD/8.png'), pygame.image.load('media/sprites/ArcherWoman/WD/9.png')]
            char = pygame.image.load('media/sprites/ArcherWoman/char.png')
            standing = pygame.image.load('media/sprites/ArcherWoman/char.png')
            return entity.Unit(State, 9, 1, 50, 50, char, standing, walkRight, walkLeft)
        if type == "ElfWoman":
            walkRight = [pygame.image.load('media/sprites/ElfWoman/WR/1.png'), pygame.image.load('media/sprites/ElfWoman/WR/2.png'), pygame.image.load('media/sprites/ElfWoman/WR/3.png'), pygame.image.load('media/sprites/ElfWoman/WR/4.png'), pygame.image.load('media/sprites/ElfWoman/WR/5.png'), pygame.image.load('media/sprites/ElfWoman/WR/6.png'), pygame.image.load('media/sprites/ElfWoman/WR/7.png'), pygame.image.load('media/sprites/ElfWoman/WR/8.png'), pygame.image.load('media/sprites/ElfWoman/WR/9.png')]
            walkUp = [pygame.image.load('media/sprites/ElfWoman/WU/1.png'), pygame.image.load('media/sprites/ElfWoman/WU/2.png'), pygame.image.load('media/sprites/ElfWoman/WU/3.png'), pygame.image.load('media/sprites/ElfWoman/WU/4.png'), pygame.image.load('media/sprites/ElfWoman/WU/5.png'), pygame.image.load('media/sprites/ElfWoman/WU/6.png'), pygame.image.load('media/sprites/ElfWoman/WU/7.png'), pygame.image.load('media/sprites/ElfWoman/WU/8.png'), pygame.image.load('media/sprites/ElfWoman/WU/9.png')]
            walkLeft = [pygame.image.load('media/sprites/ElfWoman/WL/1.png'), pygame.image.load('media/sprites/ElfWoman/WL/2.png'), pygame.image.load('media/sprites/ElfWoman/WL/3.png'), pygame.image.load('media/sprites/ElfWoman/WL/4.png'), pygame.image.load('media/sprites/ElfWoman/WL/5.png'), pygame.image.load('media/sprites/ElfWoman/WL/6.png'), pygame.image.load('media/sprites/ElfWoman/WL/7.png'), pygame.image.load('media/sprites/ElfWoman/WL/8.png'), pygame.image.load('media/sprites/ElfWoman/WL/9.png')]
            walkDown = [pygame.image.load('media/sprites/ElfWoman/WD/1.png'), pygame.image.load('media/sprites/ElfWoman/WD/2.png'), pygame.image.load('media/sprites/ElfWoman/WD/3.png'), pygame.image.load('media/sprites/ElfWoman/WD/4.png'), pygame.image.load('media/sprites/ElfWoman/WD/5.png'), pygame.image.load('media/sprites/ElfWoman/WD/6.png'), pygame.image.load('media/sprites/ElfWoman/WD/7.png'), pygame.image.load('media/sprites/ElfWoman/WD/8.png'), pygame.image.load('media/sprites/ElfWoman/WD/9.png')]
            char = pygame.image.load('media/sprites/ElfWoman/char.png')
            standing = pygame.image.load('media/sprites/ElfWoman/char.png')
            return entity.Unit(State, 9, 2, 50, 50, char, standing, walkRight, walkLeft)
        if type == "SpearsMan":
            walkRight = [pygame.image.load('media/sprites/SpearsMan/WR/1.png'), pygame.image.load('media/sprites/SpearsMan/WR/2.png'), pygame.image.load('media/sprites/SpearsMan/WR/3.png'), pygame.image.load('media/sprites/SpearsMan/WR/4.png'), pygame.image.load('media/sprites/SpearsMan/WR/5.png'), pygame.image.load('media/sprites/SpearsMan/WR/6.png'), pygame.image.load('media/sprites/SpearsMan/WR/7.png'), pygame.image.load('media/sprites/SpearsMan/WR/8.png'), pygame.image.load('media/sprites/SpearsMan/WR/9.png')]
            walkUp = [pygame.image.load('media/sprites/SpearsMan/WU/1.png'), pygame.image.load('media/sprites/SpearsMan/WU/2.png'), pygame.image.load('media/sprites/SpearsMan/WU/3.png'), pygame.image.load('media/sprites/SpearsMan/WU/4.png'), pygame.image.load('media/sprites/SpearsMan/WU/5.png'), pygame.image.load('media/sprites/SpearsMan/WU/6.png'), pygame.image.load('media/sprites/SpearsMan/WU/7.png'), pygame.image.load('media/sprites/SpearsMan/WU/8.png'), pygame.image.load('media/sprites/SpearsMan/WU/9.png')]
            walkLeft = [pygame.image.load('media/sprites/SpearsMan/WL/1.png'), pygame.image.load('media/sprites/SpearsMan/WL/2.png'), pygame.image.load('media/sprites/SpearsMan/WL/3.png'), pygame.image.load('media/sprites/SpearsMan/WL/4.png'), pygame.image.load('media/sprites/SpearsMan/WL/5.png'), pygame.image.load('media/sprites/SpearsMan/WL/6.png'), pygame.image.load('media/sprites/SpearsMan/WL/7.png'), pygame.image.load('media/sprites/SpearsMan/WL/8.png'), pygame.image.load('media/sprites/SpearsMan/WL/9.png')]
            walkDown = [pygame.image.load('media/sprites/SpearsMan/WD/1.png'), pygame.image.load('media/sprites/SpearsMan/WD/2.png'), pygame.image.load('media/sprites/SpearsMan/WD/3.png'), pygame.image.load('media/sprites/SpearsMan/WD/4.png'), pygame.image.load('media/sprites/SpearsMan/WD/5.png'), pygame.image.load('media/sprites/SpearsMan/WD/6.png'), pygame.image.load('media/sprites/SpearsMan/WD/7.png'), pygame.image.load('media/sprites/SpearsMan/WD/8.png'), pygame.image.load('media/sprites/SpearsMan/WD/9.png')]
            char = pygame.image.load('media/sprites/SpearsMan/char.png')
            standing = pygame.image.load('media/sprites/SpearsMan/char.png')
            return entity.Unit(State, 9, 3, 50, 50, char, standing, walkRight, walkLeft)
        if type == "WizardMan":
            walkRight = [pygame.image.load('media/sprites/WizardMan/WR/1.png'), pygame.image.load('media/sprites/WizardMan/WR/2.png'), pygame.image.load('media/sprites/WizardMan/WR/3.png'), pygame.image.load('media/sprites/WizardMan/WR/4.png'), pygame.image.load('media/sprites/WizardMan/WR/5.png'), pygame.image.load('media/sprites/WizardMan/WR/6.png'), pygame.image.load('media/sprites/WizardMan/WR/7.png'), pygame.image.load('media/sprites/WizardMan/WR/8.png'), pygame.image.load('media/sprites/WizardMan/WR/9.png')]
            walkUp = [pygame.image.load('media/sprites/WizardMan/WU/1.png'), pygame.image.load('media/sprites/WizardMan/WU/2.png'), pygame.image.load('media/sprites/WizardMan/WU/3.png'), pygame.image.load('media/sprites/WizardMan/WU/4.png'), pygame.image.load('media/sprites/WizardMan/WU/5.png'), pygame.image.load('media/sprites/WizardMan/WU/6.png'), pygame.image.load('media/sprites/WizardMan/WU/7.png'), pygame.image.load('media/sprites/WizardMan/WU/8.png'), pygame.image.load('media/sprites/WizardMan/WU/9.png')]
            walkLeft = [pygame.image.load('media/sprites/WizardMan/WL/1.png'), pygame.image.load('media/sprites/WizardMan/WL/2.png'), pygame.image.load('media/sprites/WizardMan/WL/3.png'), pygame.image.load('media/sprites/WizardMan/WL/4.png'), pygame.image.load('media/sprites/WizardMan/WL/5.png'), pygame.image.load('media/sprites/WizardMan/WL/6.png'), pygame.image.load('media/sprites/WizardMan/WL/7.png'), pygame.image.load('media/sprites/WizardMan/WL/8.png'), pygame.image.load('media/sprites/WizardMan/WL/9.png')]
            walkDown = [pygame.image.load('media/sprites/WizardMan/WD/1.png'), pygame.image.load('media/sprites/WizardMan/WD/2.png'), pygame.image.load('media/sprites/WizardMan/WD/3.png'), pygame.image.load('media/sprites/WizardMan/WD/4.png'), pygame.image.load('media/sprites/WizardMan/WD/5.png'), pygame.image.load('media/sprites/WizardMan/WD/6.png'), pygame.image.load('media/sprites/WizardMan/WD/7.png'), pygame.image.load('media/sprites/WizardMan/WD/8.png'), pygame.image.load('media/sprites/WizardMan/WD/9.png')]
            char = pygame.image.load('media/sprites/WizardMan/char.png')
            standing = pygame.image.load('media/sprites/WizardMan/char.png')
            return entity.Unit(State, 9, 4, 64, 64, char, standing, walkRight, walkLeft)
    
    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        if not hasattr(State.current_entity, 'take_turn'): #entities with an AI component are not player-controlled
            if self.action == None:
                eh.handle_combat_events(self, eventList)
            elif self.action == 'move':
                eh.handle_movement_events(self, eventList)
            elif self.action == 'attack':
                eh.handle_attack_events(self, eventList)
        else:
            current_entity.take_turn()
        
    def render(self):
        self.r.render_background()
        self.r.render_entities(self.entities)
        self.play_next_animation()
        pygame.display.flip()

    def clean_up(self):
        print("Cleaning up combat arena")
        owner.entities = []

        

    
stateinfo = {
    'title': Title(),
    'levelSelect': LevelSelect(),
    'roster': RosterMenu(),
    'combat': Combat()
}
    
def update_state(State):
    if State.done == True:
        if State.next != None:
            temp = stateinfo[State.next]
            State.next = None
            State.done = False
            State.clean_up()
            return temp
    else:
        return State
    
            
            
