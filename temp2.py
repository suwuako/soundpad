import asyncio
import winsound
import keyboard

async def play(path):
    winsound.PlaySound(path, winsound.SND_ALIAS)

def listen(k):
    print(k)

def main():
    #r'data/basic.wav'
    in_use = []
    keyboard.add_hotkey('q', listen(1))
    while True:
        pass
main()
