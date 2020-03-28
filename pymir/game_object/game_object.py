import pygame
from ..base_object import base_object

class game_object(base_object):
    def __init__(self, **args):
        self.setup_initial_arguments()
        super(game_object, self).__init__(args = args)

    def setup_initial_arguments(self):
        self.initial_arguments({
            'parent': None,
            'screen': None
        })