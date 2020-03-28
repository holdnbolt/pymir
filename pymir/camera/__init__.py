import pygame

class camera:
    def __init__(self):
        
        self.height = None
        self.screen = None
        self.width = None

    def set_resolution(self, resolution = 720, ratio = '16:9'):
        diff = ratio.split(":")
        diff = float(diff[1]) / float(diff[0])
        self.height = resolution
        self.width = int(resolution / diff)

    def start(self):
        if not self.width or not self.height:
            self.set_resolution()

        pygame.init()
        print(self.width)