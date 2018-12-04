import sys, pygame, logic

def handle_system_events(State, eventList):
    for event in eventList:
        if event.type == pygame.QUIT:
            State.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                State.quit = True


def handle_title_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            State.done = True
            State.next = 'levelSelect'

def handle_level_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                State.done = True
                State.next = 'combat1'
            if event.key == pygame.K_2:
                State.done = True
                State.next = 'combat2'
            if event.key == pygame.K_3:
                State.done = True
                State.next = 'combat3'
            if event.key == pygame.K_RETURN:
                State.done = True
                State.next = 'title'

def handle_roster_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                State.done = True
                State.next = 'title'

def handle_combat_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                print("attack state")
                State.action = 'attack'
            if event.key == pygame.K_c:
                print("move state")
                State.action = 'move'

def handle_movement_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_LEFT:
                    State.current_entity.move_guide('left')
                if event.key == pygame.K_RIGHT:
                    State.current_entity.move_guide('right')
                if event.key == pygame.K_UP:
                    State.current_entity.move_guide('up')
                if event.key == pygame.K_DOWN:
                    State.current_entity.move_guide('down')
                if event.key == pygame.K_RETURN:
                    State.current_entity.move()
            except AttributeError as e:
                print("Entity cannot move!")
                print(e)

def handle_attack_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_a:
                    State.current_entity.game.animations.append(("attack", State.current_entity))
                if event.key == pygame.K_d:
                    State.current_entity.game.animations.append(("die", State.current_entity))
                if event.key == pygame.K_LEFT:
                    State.current_entity.attack_guide('left')
                if event.key == pygame.K_RIGHT:
                    State.current_entity.attack_guide('right')
                if event.key == pygame.K_UP:
                    State.current_entity.attack_guide('up')
                if event.key == pygame.K_DOWN:
                    State.current_entity.attack_guide('down')
                if event.key == pygame.K_RETURN:
                    print(State.current_entity)
                    
                    State.current_entity.deal_damage()
            except AttributeError as e:
                print("Entity cannot attack!")
                print(e)
                
