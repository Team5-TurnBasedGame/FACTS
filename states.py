import pygame as pg
import sys

class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

class Menu(States):
    def __init__(self):
        States.__init__(self)

    def cleanup(self):
        print('cleaning up Menu state stuff')

    def startup(self):
        print('starting Menu state stuff')

    def get_event(self, event):
        keys = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if keys[pg.K_LEFT]:
                self.done = True
                print("left")
                self.next = 'menu2'

        if event.type == pg.KEYDOWN:
            if event.type == pg.KEYDOWN:
                if keys[pg.K_RIGHT]:
                    self.done = True
                    self.next = 'game'

    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((255,0,0))


class Menu2(States):
    def __init__(self):
        States.__init__(self)

    def cleanup(self):
        print('cleaning up Menu state stuff')
    def startup(self):
        print('starting Menu state stuff')
    def get_event(self, event):
        keys = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if keys[pg.K_LEFT]:
                self.done = True
                print("left")
                self.next = 'menu'

        if event.type == pg.KEYDOWN:
            if event.type == pg.KEYDOWN:
                if keys[pg.K_RIGHT]:
                    self.done = True
                    self.next = 'game'

    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((150,0,0))

class Game(States):
    def __init__(self):
        States.__init__(self)
    def cleanup(self):
        print('cleaning up Menu state stuff')

    def startup(self):
        print('starting Menu state stuff')

    def get_event(self, event):
        keys = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if keys[pg.K_LEFT]:
                self.done = True
                print("left")
                self.next = 'menu2'

        if event.type == pg.KEYDOWN:
            if event.type == pg.KEYDOWN:
                if keys[pg.K_RIGHT]:
                    self.done = True
                    self.next = 'menu'
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,255))

class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()


if __name__ == '__main__':
    settings = {
        'size':(600,400),
        'fps' :60
    }

    app = Control(**settings)
    state_dict = {
        'menu': Menu(),
        'game': Game(),
        'menu2':Menu2()
    }
    app.setup_states(state_dict, 'menu')
    print("blah")
    app.main_game_loop()
    print("blah")
    pg.quit()
sys.exit()