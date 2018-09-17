from microbit import *
import music

while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    reading_z = accelerometer.get_z()
    if reading_x > 100:
        music.play("A1:2")
    elif 100 > reading_x > 20:
        music.play("B1:2")
    elif reading_x < -20:
        music.play("C1:2")
    elif reading_y > 100:
        music.play("D1:2")
    elif 100 > reading_y > 20:
        music.play("E1:2")
    elif reading_y < -20:
        music.play("F1:2")
    elif reading_z > 100:
        music.play("G1:2")
    elif 100 > reading_z > 20:
        music.play("A2:2")
    elif reading_z < -20:
        music.play("B2:2")
    else:
        music.play(music.ENTERTAINER)
