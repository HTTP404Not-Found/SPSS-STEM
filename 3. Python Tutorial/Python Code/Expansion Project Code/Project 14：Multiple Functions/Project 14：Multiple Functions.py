from microbit import *
import music
import neopixel
LCD_I2C_ADDR=0x27
display.show(Image.HAPPY)
pin16.write_digital(0)
np = neopixel.NeoPixel(pin14, 4)
class LCD1602():
    def __init__(self):
        self.buf = bytearray(1)
        self.BK = 0x08
        self.RS = 0x00
        self.E = 0x04
        self.setcmd(0x33)
        sleep(5)
        self.send(0x30)
        sleep(5)
        self.send(0x20)
        sleep(5)
        self.setcmd(0x28)
        self.setcmd(0x0C)
        self.setcmd(0x06)
        self.setcmd(0x01)
        self.version='1.0'

    def setReg(self, dat):
        self.buf[0] = dat
        i2c.write(LCD_I2C_ADDR, self.buf)
        sleep(1)

    def send(self, dat):
        d=dat&0xF0
        d|=self.BK
        d|=self.RS
        self.setReg(d)
        self.setReg(d|0x04)
        self.setReg(d)

    def setcmd(self, cmd):
        self.RS=0
        self.send(cmd)
        self.send(cmd<<4)

    def setdat(self, dat):
        self.RS=1
        self.send(dat)
        self.send(dat<<4)

    def clear(self):
        self.setcmd(1)

    def backlight(self, on):
        if on:
            self.BK=0x08
        else:
            self.BK=0
        self.setcmd(0)

    def on(self):
        self.setcmd(0x0C)

    def off(self):
        self.setcmd(0x08)

    def shl(self):
        self.setcmd(0x18)

    def shr(self):
        self.setcmd(0x1C)

    def char(self, ch, x=-1, y=0):
        if x>=0:
            a=0x80
            if y>0:
                a=0xC0
            a+=x
            self.setcmd(a)
        self.setdat(ch)

    def puts(self, s, x=0, y=0):
        if len(s)>0:
            self.char(ord(s[0]),x,y)
            for i in range(1, len(s)):
                self.char(ord(s[i]))
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)
l = LCD1602()
l.clear()
Servo(pin9).write_angle(90)
Servo(pin8).write_angle(0)
display.show(Image.HAPPY)
pin12.write_digital(0)
pin13.write_digital(0)
np.clear()
while True:
    if pin0.read_analog() > 400:
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
        sleep(1000)
        for pixel_id2 in range(0, len(np)):
            np[pixel_id2] = (255, 165, 0)
            np.show()
        sleep(1000)
        for pixel_id3 in range(0, len(np)):
            np[pixel_id3] = (255, 255, 0)
            np.show()
        sleep(1000)
        for pixel_id4 in range(0, len(np)):
            np[pixel_id4] = (0, 255, 0)
            np.show()
        sleep(1000)
        for pixel_id5 in range(0, len(np)):
            np[pixel_id5] = (0, 0, 255)
            np.show()
        sleep(1000)
        for pixel_id6 in range(0, len(np)):
            np[pixel_id6] = (75, 0, 130)
            np.show()
        sleep(1000)
        for pixel_id7 in range(0, len(np)):
            np[pixel_id7] = (238, 130, 238)
            np.show()
        sleep(1000)
        for pixel_id8 in range(0, len(np)):
            np[pixel_id8] = (160, 32, 240)
            np.show()
        sleep(1000)
        for pixel_id9 in range(0, len(np)):
            np[pixel_id9] = (255, 255, 255)
        sleep(1000)
        np.clear()
        sleep(1000)
        Servo(pin9).write_angle(0)
        sleep(3000)
        Servo(pin8).write_angle(120)
        sleep(3000)
        pin12.write_digital(1)
        pin13.write_digital(0)
        sleep(5000)
    else:
        music.reset()
        pin16.write_digital(0)
        Servo(pin9).write_angle(90)
        sleep(200)
        Servo(pin8).write_angle(0)
        sleep(200)
        pin12.write_digital(0)
        pin13.write_digital(0)
        np.clear()
    if pin1.read_digital() == 0:
        l.puts("MQ-2:", 1, 0)
        l.puts("gas leakage", 1, 1)
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
        sleep(200)
    else:
        l.clear()
        music.reset()
        pin16.write_digital(0)
