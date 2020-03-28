import pygame
from ..base_object import base_object

class game_window(base_object):
    def __init__(self, **args):
        self.set_initial_arguments()
        super(game_window, self).__init__(**args)

        self.single_object = None
        self.screen = None

    def attach_object(self, single_object):
        self.single_object = single_object
        self.single_object.parent = self

    def end(self):
        pygame.quit()

    def initialize(self):
        if not self.width or not self.height:
            print("Failure to initialize window")
            exit(-1)

        if self.screen:
            self.end()

        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])

    def set_initial_arguments(self):
        self.initial_arguments({
            'height': None,
            'width': None,
            'parent': None
        })

    def set_resolution(self, resolution = 720, ratio = '16:9'):
        diff = ratio.split(":")
        diff = float(diff[1]) / float(diff[0])
        self.height = resolution
        self.width = int(resolution / diff)

    def start(self):
        if not self.width or not self.height:
            self.set_resolution()
        
        self.initialize()

    def update(self):
        self.screen.fill([0, 0, 0])
        if self.single_object:
            self.single_object.update()
        pygame.display.update()