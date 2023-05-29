import keyboard
import winsound

while True:
    if keyboard.is_pressed('q'):
        winsound.PlaySound(r'data/basic.wav', winsound.SND_FILENAME)
