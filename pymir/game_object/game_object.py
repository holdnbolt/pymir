import pygame
from ..base_object import base_object

class game_object(base_object):
    def __init__(self, **args):
        self.set_initial_arguments()
        super(game_object, self).__init__(**args)

        if not self.no_image and not self.screen:
            self.screen = pygame.Surface([self.width, self.height])
            self.screen.fill([0, 0, 190])

    def draw(self):
        if not self.parent:
            return False

        if len(self.children) > 0:
            pass
        
        self.parent.screen.blit(self.screen, (self.x, self.y))

    def move(self, x = 0, y = 0):
        self.x += x
        self.y += y

    def set_initial_arguments(self):
        self.initial_arguments({
            'children': [],
            'height': 32,
            'no_image': False,
            'parent': None,
            'screen': None,
            'spritesheet': None,
            'width': 32,
            'x': 0,
            'y': 0
        })

    def update(self):
        self.move(15, 15)
        self.draw()