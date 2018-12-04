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
        if level == 1:
            State.entities.append(units.make_swordsman(self, 4, 4))
            State.entities.append(units.make_archerwoman(self, 9, 1))
            #State.entities.append(units.make_elfwoman(self, 9, 2))
            #State.entities.append(units.make_spearman(self, 9, 3))
            #State.entities.append(units.make_wizardman(self, 9, 4))
            State.entities.append(units.make_GoblinMan(self, 1,4))
            State.entities.append(units.make_TrollMan(self, 1,5))
        elif level == 2:
            State.entities.append(units.make_archerwoman(self, 4, 4))
            State.entities.append(units.make_archerwoman(self, 9, 1))
            State.entities.append(units.make_TrollMan(self, 1,5))
        elif level == 3:
            State.entities.append(units.makewizardman(self, 1, 5))
            State.entities.append(units.make_GoblinMan(self, 1,4))
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
        if playerAllDead: print("game over you lose")
        return playerAllDead
        

    def enemy_gameover(self):
        enemyAllDead = True
        for e in self.entities:
            if e.team == 'enemy':
                enemyAllDead = False
        if enemyAllDead: print("you win!")
        return enemyAllDead
        
    
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
            State.next = None
            State.done = False
            State.clean_up()
            return temp
    else:
        return State
    
            
            
