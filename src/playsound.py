import winsound
import sys
import asyncio
import os
import sys

import src.write_json as write_json
import src.read_json as read_json

def play(path):
    """
    :param path: path to sound file
    :return: None
    """
    abs_path = os.path.abspath(os.getcwd())

    # Access path loads all current playing sounds
    access_path = f"{abs_path}\data\in_use\in_use.json"

    in_use = read_json.read(access_path)

    if path not in in_use:
        # writes sound to be played into file to prevent keyboard presses causing multiple inputs
        in_use.append(path)
        write_json.write(access_path, in_use)

        # Plays the sound through sound system
        winsound.PlaySound(path, winsound.SND_ALIAS)

        # Reads what is currently being played so that new inputted values don't get overwritten and removes played
        # sound so it can be played again
        new_write = read_json.read(access_path)
        new_write.remove(path)
        write_json.write(access_path, new_write)

if __name__ == "__main__":
    #ARG here is set to 1 as a constant because of the command-line passed argument being the second index in the array
    ARG = 1
    path = sys.argv[ARG]
    # read passed argument from os_pipe (which is the path) as a shell passed argument
    path = sys.argv[1]
    play(path)