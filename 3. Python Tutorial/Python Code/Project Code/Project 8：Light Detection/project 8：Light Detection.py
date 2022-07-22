from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(50)

    if display.read_light_level() <= 20:
        display.show(Image("00990:""09900:""09900:""09900:""00990"))
    else:
        display.show(Image("90909:""09990:""99999:""09990:""90909"))
