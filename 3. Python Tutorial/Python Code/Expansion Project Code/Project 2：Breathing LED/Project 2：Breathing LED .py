from microbit import *

display.show(Image.HAPPY)

pin16.write_digital(0)

while True:
    for index in range (0, 255):
        pin16.write_analog(index)
        sleep(10)
    for index in range (0, 255):
        pin16.write_analog(255-index)
        sleep(10)

