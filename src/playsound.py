import winsound
import asyncio

def play(path):
    winsound.PlaySound(path, winsound.SND_ALIAS)

if __name__ == "__main__":
    path = input()
    print(path)
    play(path)