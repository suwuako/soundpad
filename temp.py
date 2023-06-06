import keyboard
import winsound

def play(path):
    winsound.PlaySound(path, winsound.SND_ALIAS)

keyboard.add_hotkey("q", lambda: play('data/basic.wav'))
keyboard.add_hotkey("w", lambda: play('data/flam.wav'))


while True:
    v=0