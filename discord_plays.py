import time
from games import mario


async def play_mario(message_value):
    if message_value == 'jump':
        await mario.jump()
    if message_value == 'left':
        await mario.left()
    if message_value == 'lightleft':
        await mario.lightleft()
    if message_value == 'right':
        await mario.right()
    if message_value == 'lightright':
        await mario.lightright()
    if message_value == 'start':
        await mario.start()
    if message_value == 'stop':
        await mario.stop()
    if message_value == 'rump':
        await mario.rump()
    if message_value == 'lump':
        await mario.lump()
    if message_value == 'sprint':
        await mario.sprint()
    if message_value == 'stopsprint':
        await mario.stopsprint()
    if message_value == 'fire':
        await mario.stopsprint()
