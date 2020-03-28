import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from . import camera as pymir_camera

def camera():
    return pymir_camera.camera()