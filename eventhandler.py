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
            if event.key == pygame.K_LEFT:
                State.done = True
                State.next = 'turn'

def handle_level_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                State.done = True
                State.next = 'roster'
            if event.key == pygame.K_RIGHT:
                State.done = True
                State.next = 'title'

def handle_roster_events(State, eventList):
    for event in eventList:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                State.done = True
                State.next = 'title'
