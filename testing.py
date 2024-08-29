#Ignore this ms ghent im just figuring out keyboards, ill test applying this tommorow (08/30/24)

import keyboard

while True:
    try:
        if keyboard.is_pressed("f"):
            print("end")
    except:
        break