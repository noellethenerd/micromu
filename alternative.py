from microbit import*
import music

while True:
    reading_x = accelerometer.get_x()
    if 40 > reading_x > 20:
        display.show("R")
        music.play("A1:2")
    elif reading_x < -20:
        display.show("L")
        music.play("A3:2")
