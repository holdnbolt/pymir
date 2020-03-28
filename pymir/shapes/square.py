from ..base_object import base_object
import pygame

class square(base_object):
    def __init__(self, width = 32, height = 32):
        self.screen = pygame.Surface([width, height])

    def draw(self):
        return self.screen