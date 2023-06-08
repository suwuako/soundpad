import keyboard
import os
import pathlib
import asyncio

from src import playsound
from src import read_json

from src import sound_handler
from src import os_pipe

# def listener(key):
#     print("pass")
#     pass

async def listener(thread):
    keymap = read_json.read('data/keymap.json')
    print(f'Listener running on thread {thread}')

    key_list = list()
    path_list = list()

    for key, path in keymap.items():
        key_list.append(key)
        path_list.append(path)
        if keyboard.is_pressed(key):
            # needs to pipe arguments into os_pipe which runs a separate subprocess because playing audio pauses python
            # until audio is done playing
            os_pipe.play(path)
    return






def load():
    keymap = read_json.read('data/keymap.json')


    # print("loading")
    # for key, path in keymap.items():a
    #     print(f"Syncing {key} to {path}")
    #     keyboard.add_hotkey(key, lambda: playsound.play(path))
    #     print("doneq")
    #
    # print("complete")

