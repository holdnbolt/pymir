import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from . import camera as pymir_camera
from . import game_object
from . import instance as pymir_instance
from . import room as pymir_room


def camera(**args):
    return pymir_camera.main_camera(**args)

def clock(**args):
    pass

def collisions(**args):
    pass

def gobject(**args):
    return game_object.game_object(**args)

def instance(**args):
    return pymir_instance.game_instance(**args)

def room(**args):
    return pymir_room.game_room(**args)

def world(**args):
    pass