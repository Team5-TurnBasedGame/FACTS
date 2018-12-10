import sys
import pygame
import entity
import units
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

    def initialize(self):
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
        while len(self.animations): #wait for animation queue to empty
            self.play_next_animation()
        current_index = self.entities.index(self.current_entity)
        if current_index+1 < len(self.entities):
            self.current_entity = self.entities[current_index + 1]
        else:
            self.current_entity = self.entities[0]

class Title(State):
    def __init__(self):
        State.__init__(self)
        pygame.mixer.init(44100, -16, 2, 2048)
        pygame.mixer.music.load('media/menu.mp3')
        pygame.mixer.music.play(-1)


    def initialize(self):
        pass

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_title_events(self, eventList)

    def resolve_changes(self):
        pass

    def render(self):
        self.r.render_background()
        self.r.render_title_screen()
        pygame.display.flip()


    def clean_up(self):
        print("Cleaning up title")

class LevelSelect(State):
    def __init__(self):
        State.__init__(self)


    def initialize(self):
        pass

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_level_events(self, eventList)

    def resolve_changes(self):
        pass

    def render(self):
        self.r.render_background()
        self.r.renderLevelSelect()
        pygame.display.flip()

    def clean_up(self):
        print("Cleaning up levelSelect")

class RosterMenu(State):
    def __init__(self):
        State.__init__(self)

    def initialize(self):
        pass

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        eh.handle_roster_events(self, eventList)

    def resolve_changes(self):
        pass

    def render(self):
        print("nothing to render")
        
    def clean_up(self):
            print("Cleaning up rosterMenu")

class Combat(State):
    def __init__(self, level):
        State.__init__(self)
        self.level = level
        
    def initialize(self):
        print(str(self.level))
        if self.level == 1:
            print("Level 1")
            State.entities.append(units.make_swordsman(self, 1, 2))
            State.entities.append(units.make_swordsman(self, 3, 5))
            State.entities.append(units.make_swordsman(self, 1, 8))
            State.entities.append(units.make_TrollMan(self, 9, 2))
            State.entities.append(units.make_TrollMan(self, 9, 5))
            State.entities.append(units.make_TrollMan(self, 9, 8))
        elif self.level == 2:
            print("Level 2")
            State.entities.append(units.make_archerwoman(self, 1, 3))
            State.entities.append(units.make_archerwoman(self, 4, 6))
            State.entities.append(units.make_archerwoman(self, 5, 2))
            State.entities.append(units.make_swordsman(self, 5, 6))  
            State.entities.append(units.make_GoblinMan(self, 9,4))
            State.entities.append(units.make_GoblinMan(self, 8,7))
            State.entities.append(units.make_GoblinMan(self, 9,7))
        elif self.level == 3:
            print("Level 3")
            State.entities.append(units.make_wizardman(self, 1, 5))
            State.entities.append(units.make_archerwoman(self, 1, 3))
            State.entities.append(units.make_swordsman(self, 2, 6))  
            State.entities.append(units.make_spearman(self, 3, 6))
            State.entities.append(units.make_elfwoman(self, 1, 9))  
            
            State.entities.append(units.make_GoblinMan(self, 9,9))
            State.entities.append(units.make_GoblinMan(self, 9,2))
            State.entities.append(units.make_GoblinMan(self, 8,4))
            State.entities.append(units.make_GoblinMan(self, 7,5))
            State.entities.append(units.make_TrollMan(self, 8,2))
            State.entities.append(units.make_TrollMan(self, 9,6))
            State.entities.append(units.make_TrollMan(self, 7,9))
            State.entities.append(units.make_TrollMan(self, 8,9))
            State.entities.append(units.make_OrkMan(self, 7,4))
            State.entities.append(units.make_OrkMan(self, 8,1))
            State.entities.append(units.make_OrkMan(self, 6,9))
            State.entities.append(units.make_OrkMan(self, 9,4))
        else:
            print("Error! Invalid level!")

        State.current_entity = State.entities[0]

        self.action = None

    def handle_events(self):
        eventList = pygame.event.get()
        eh.handle_system_events(self, eventList)
        if self.current_entity.team == 'player': #entities with an AI component are not player-controlled
            if self.action == None:
                self.action = 'move'
            elif self.action == 'move':
                eh.handle_movement_events(self, eventList)
            elif self.action == 'attack':
                eh.handle_attack_events(self, eventList)
        elif self.current_entity.team == 'enemy':
            self.current_entity.take_turn()
        else:
            self.next_entity()

    def resolve_changes(self):
        for e in self.entities:
            if e.hp <= 0 and e.team != 'dead':
                e.die()
        if self.player_gameover():
            self.done = True
            self.next = 'levelSelect'
        elif self.enemy_gameover():
            self.done = True
            self.next = 'levelSelect'
        else:
            pass
        
    def render(self):
        self.r.render_background()
        self.r.render_entities(self.entities)
        self.play_next_animation()
        pygame.display.flip()

    def clean_up(self):
        print("Cleaning up combat arena")
        self.entities = []
        self.animations = []

    def player_gameover(self):
        playerAllDead = True
        for e in self.entities:
            if e.team == 'player':
                playerAllDead = False
        if playerAllDead:
            print("game over you lose")
            self.animations.append(("lose", None))
        return playerAllDead
        pygame.mixer.music.stop()
        pygame.mixer.music.load('media/level.mp3')
        pygame.mixer.music.play(-1)
        

    def enemy_gameover(self):
        enemyAllDead = True
        for e in self.entities:
            if e.team == 'enemy':
                enemyAllDead = False
        if enemyAllDead:
            print("you win!")
            self.animations.append(("win", None))
        return enemyAllDead
        pygame.mixer.music.stop()
        pygame.mixer.music.load('media/level1.mp3')
        pygame.mixer.music.play(-1)
        
    
stateinfo = {
    'title': Title(),
    'levelSelect': LevelSelect(),
    'roster': RosterMenu(),
    'combat1': Combat(1),
    'combat2': Combat(2),
    'combat3': Combat(3)
}
    
def update_state(State):
    if State.done == True:
        if State.next != None:
            temp = stateinfo[State.next]
            temp.initialize()
            State.next = None
            State.done = False
            State.clean_up()
            return temp
    else:
        return State
    
            
            
