import keyboard
import os
import pathlib
import asyncio

from src import playsound
from src import read_json

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
            localpath = os.path.abspath(os.getcwd())
            print(localpath)
            os.system(f"{localpath}/src/playsound.py {path}")






def load():
    keymap = read_json.read('data/keymap.json')


    # print("loading")
    # for key, path in keymap.items():a
    #     print(f"Syncing {key} to {path}")
    #     keyboard.add_hotkey(key, lambda: playsound.play(path))
    #     print("doneq")
    #
    # print("complete")

