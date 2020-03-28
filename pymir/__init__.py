import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from . import camera as pymir_camera
from . import instance as pymir_instance
from . import game_object

def camera():
    return pymir_camera.main_camera()

# def instance():
#     return pymir_instance.game_instance()

def gobject():
    return game_object.gobject()