from microbit import *

pin12.write_digital(0)
pin13.write_digital(0)

while True:
    pin12.write_digital(1)
    pin13.write_analog(600)
    sleep(5000)
    pin12.write_digital(0)
    pin13.write_analog(0)
    sleep(1000)
    pin12.write_digital(0)
    pin13.write_analog(400)
    sleep(5000)
    pin12.write_digital(1)
    pin13.write_analog(1023)
    sleep(1000)

