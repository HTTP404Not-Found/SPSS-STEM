from microbit import *

display.show(Image.HAPPY)

while True:
    val = pin1.read_digital()
    print("digital signal:", val)
    sleep(100)
