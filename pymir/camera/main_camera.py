import pygame
from ..base_object import base_object
from . import window

class camera(base_object):
    def __init__(self, **args):
        self.set_initial_arguments()
        super(camera, self).__init__(**args)
        
        if self.window:
            self.main_window = window.game_window()

    def attach_object(self, single_object):
        self.main_window.attach_object(single_object)

    def set_initial_arguments(self):
        self.initial_arguments({
            'parent': None,
            'resolution': 720,
            'window': True,
            'window_ratio': '16:9'
        })

    def start(self):
        self.main_window.set_resolution(self.resolution, self.window_ratio)
        self.main_window.start()

    def update(self):
        self.main_window.update()