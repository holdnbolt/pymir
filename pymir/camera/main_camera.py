import pygame
from ..base_object import base_object

class camera(base_object):
    def __init__(self, **args):
        super(camera, self).__init__()
        self.height = None
        self.screen = None
        self.width = None

        pygame.init()

    def set_resolution(self, resolution = 720, ratio = '16:9'):
        diff = ratio.split(":")
        diff = float(diff[1]) / float(diff[0])
        self.height = resolution
        self.width = int(resolution / diff)

    def start(self):
        if not self.width or not self.height:
            self.set_resolution()

        self.screen = pygame.display.set_mode([self.width, self.height])