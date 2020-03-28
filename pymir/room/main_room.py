import pygame
from ..base_object import base_object

class game_room(base_object):
    def __init__(self, **args):
        super(game_room, self).__init__(**args)
        self.setup_args(args = args)

    def parse_args(self, args):
        if len(args) > 0:
            print(args)