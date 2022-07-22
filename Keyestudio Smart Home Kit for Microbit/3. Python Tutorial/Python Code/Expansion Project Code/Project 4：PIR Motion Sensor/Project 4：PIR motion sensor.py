from microbit import *

val = 0

display.show(Image.HAPPY)

while True:
    val = pin15.read_digital()

    print("digital signals:", val)

    sleep(100)

