import os
import subprocess
import sys

from colorama import Fore, Back, Style, init

def play(path):
    """
    :param path: Path to sound file
    :return: None
    """
    init(autoreset=True)

    # pipe into playsound whcih opens a new python instance that doesn't hold up the stack
    # finds local path absolute to its location through os
    localpath = f"{os.path.abspath(os.getcwd())}\src\playsound.py"
    path = f"{os.path.abspath(os.getcwd())}\{path}"

    # opens a new process separate from current running process and automatically closes itself after playing sound
    # localpath represents file executable to playsound.py and sys.executable runs it as a python file
    subprocess.Popen([sys.executable, localpath, path], stderr=subprocess.PIPE)
    print(f"{Fore.GREEN}Playing sound file at: {path}\n",
            f"{Fore.RED}Press Control+C to stop the soundpad")
