from microbit import sleep, pin12
import neopixel

np = neopixel.NeoPixel(pin12, 4)
while True:
    for i in range(256):
        for j in range(4):
            np[j] = (i, 0, 0)
        np.show()
        sleep(10)
    for i in range(256):
        for j in range(4):
            np[j] = (255 - i, 0, 0)
        np.show()
        sleep(10)
