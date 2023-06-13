from os import walk

def run():
    """
    lists keymaps in /data/
    :return: None
    """
    files = []
    filenames = []

    for (dirpath, dirnames, filenames) in walk("data"):
        files.extend(filenames)

    print("Here are all your layouts:")
    for i in files:
        # Delete the .json file extension
        filename = i[:-5]
        print(filename)

    input("Press enter to continue: ")
    return


