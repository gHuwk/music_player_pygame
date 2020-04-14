from pygame import mixer

mixer.init()

mixer.music.load(input("Input filename in local path: "))
mixer.music.set_volume(float(input("Set volume (float): ")))
mixer.music.play()

while True:
    print("P - Pause;\nR - Return\nE - escape\n")
    ery = input(">")

    if ery == 'P':
        mixer.music.pause()
    elif ery == 'R':
        mixer.unpause()
    elif ery == 'E':
        mixer.music.stop()
        break
