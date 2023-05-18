import keyboard
import time


def jump():
    keyboard.press("space")
    time.sleep(1)
    keyboard.release("space")


def left():
    keyboard.press("a")
    time.sleep(0.8)
    keyboard.release("a")


def lightleft():
    keyboard.press("a")
    time.sleep(0.25)
    keyboard.release("a")


def right():
    keyboard.press("d")
    time.sleep(0.8)
    keyboard.release("d")


def lightright():
    keyboard.press("d")
    time.sleep(0.25)
    keyboard.release("d")


def start():
    keyboard.press("d")


def stop():
    keyboard.release("d")


def sprint():
    keyboard.press("shift")


def stopsprint():
    keyboard.release("shift")


def rump():
    keyboard.press('d')
    time.sleep(0.2)
    keyboard.press('space')
    time.sleep(1)
    keyboard.release('space')
    keyboard.release('d')


def lump():
    keyboard.press('a')
    time.sleep(0.2)
    keyboard.press('space')
    time.sleep(1)
    keyboard.release('space')
    keyboard.release('a')


def fire():
    keyboard.press_and_release('shift')
