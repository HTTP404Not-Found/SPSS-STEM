from microbit import *

display.show(Image.HAPPY)

pin16.write_digital(0)

while True:
    pin16.write_digital(1)
    sleep(1000)
    pin16.write_digital(0)
    sleep(1000)
