from microbit import *
import music
display.show(Image.HAPPY)

pin16.write_digital(0)

while True:
    if pin0.read_analog() > 500:
        music.play("C5:4")
        pin16.write_digital(1)
        sleep(100)
        music.reset()
        pin16.write_digital(0)
        sleep(100)
        music.play("C5:4")
        pin16.write_digital(1)
        sleep(100)
        music.reset()
        pin16.write_digital(0)
        sleep(100)
    else:
        music.reset()
        pin16.write_digital(0)

