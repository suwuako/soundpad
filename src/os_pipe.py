import asyncio
import os
import subprocess
import sys

def play(path):
    # pipe into playsound whcih opens a new python instance that doesn't hold up the stack
    localpath = f"{os.path.abspath(os.getcwd())}\src\playsound.py"
    print(localpath)
    subprocess.Popen([sys.executable, localpath, path], stderr=subprocess.PIPE)
    return