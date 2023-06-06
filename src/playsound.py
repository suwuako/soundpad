import winsound

def play(path):
    winsound.PlaySound(path, winsound.SND_ALIAS)