from microbit import *

display.show(Image.HAPPY)

while True:
    val = pin0.read_analog()
    print("value:", val)
    sleep(100)
