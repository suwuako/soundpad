import keyboard
import winsound
import asyncio

async def play(path):
    print(1)
    await winsound.PlaySound(path, winsound.SND_ALIAS)
    print(2)

task1 = play('data/dog.wav')
task2 = play('data/basic.wav')

tasks = [task1, task2]

async def main():
    await asyncio.gather(*tasks)

asyncio.run(main())