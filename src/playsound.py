import winsound
import sys
import asyncio

def play(path):
    winsound.PlaySound(path, winsound.SND_ALIAS)

if __name__ == "__main__":
    #ARG here is set to 1 as a constant because of the command-line passed argument being the second index in the array
    ARG = 1
    path = sys.argv[ARG]
    print(path)
    play(path)