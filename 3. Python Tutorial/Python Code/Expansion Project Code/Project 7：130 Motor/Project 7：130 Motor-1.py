from microbit import *

pin12.write_digital(0)
pin13.write_digital(0)

while True:
    pin12.write_digital(1)
    pin13.write_digital(0)
    sleep(5000)
    pin12.write_digital(0)
    pin13.write_digital(0)
    sleep(1000)
    pin12.write_digital(0)
    pin13.write_digital(1)
    sleep(5000)
    pin12.write_digital(1)
    pin13.write_digital(1)
    sleep(1000)

