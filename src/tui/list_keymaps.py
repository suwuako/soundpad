from os import walk
from colorama import Fore, Back, Style, init

def run():
    """
    lists keymaps in /data/
    :return: None
    """
    init(autoreset=True)
    files = []
    filenames = []

    for (dirpath, dirnames, filenames) in walk("data"):
        files.extend(filenames)

    print("Here are all your layouts:")
    for i in files:
        # Delete the .json file extension
        filename = i[:-5]
        print(f"{Fore.GREEN} {filename}")

    input("Press enter to continue: ")
    return


