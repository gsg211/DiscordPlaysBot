import time
from games import mario


def play_mario(message_value):
    if message_value == 'jump':
        mario.jump()
    if message_value == 'left':
        mario.left()
    if message_value == 'lightleft':
        mario.lightleft()
    if message_value == 'right':
        mario.right()
    if message_value == 'lightright':
        mario.lightright()
    if message_value == 'start':
        mario.start()
    if message_value == 'stop':
        mario.stop()
    if message_value == 'rump':
        mario.rump()
    if message_value == 'lump':
        mario.lump()
    if message_value == 'sprint':
        mario.sprint()
    if message_value == 'stopsprint':
        mario.stopsprint()
    if message_value == 'fire':
        mario.stopsprint()
