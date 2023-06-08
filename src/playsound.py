import winsound
import sys
import asyncio
import os
import sys

def play(path):
    localpath = f"{os.path.abspath(os.getcwd())}\{path}"
    print(localpath)
    winsound.PlaySound(path, winsound.SND_ALIAS)

if __name__ == "__main__":
    #ARG here is set to 1 as a constant because of the command-line passed argument being the second index in the array
    ARG = 1
    path = sys.argv[ARG]
    # read passed argument from os_pipe (which is the path) as a shell passed argument
    path = sys.argv[1]
    print(path)
    play(path)