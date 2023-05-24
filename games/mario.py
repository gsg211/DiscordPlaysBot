import keyboard
import asyncio


async def jump():
    keyboard.press("space")
    await asyncio.sleep(1)
    keyboard.release("space")


async def left():
    keyboard.press("a")
    await asyncio.sleep(0.8)
    keyboard.release("a")


async def lightleft():
    keyboard.press("a")
    await asyncio.sleep(0.25)
    keyboard.release("a")


async def right():
    keyboard.press("d")
    await asyncio.sleep(0.8)
    keyboard.release("d")


async def lightright():
    keyboard.press("d")
    await asyncio.sleep(0.25)
    keyboard.release("d")


async def start():
    keyboard.press("d")


async def stop():
    keyboard.release("d")


async def sprint():
    keyboard.press("shift")


async def stopsprint():
    keyboard.release("shift")


async def rump():
    keyboard.press('d')
    await asyncio.sleep(0.2)
    keyboard.press('space')
    await asyncio.sleep(1)
    keyboard.release('space')
    keyboard.release('d')


async def lump():
    keyboard.press('a')
    await asyncio.sleep(0.2)
    keyboard.press('space')
    await asyncio.sleep(1)
    keyboard.release('space')
    keyboard.release('a')


async def fire():
    keyboard.press_and_release('shift')
