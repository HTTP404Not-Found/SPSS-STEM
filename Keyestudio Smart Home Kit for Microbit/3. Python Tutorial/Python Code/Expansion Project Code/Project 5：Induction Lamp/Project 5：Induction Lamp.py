from microbit import *

display.show(Image.HAPPY)

pin16.write_digital(0)

while True:
    if pin15.read_digital() == 1:

        pin16.write_digital(1)

    else:
        pin16.write_digital(0)
