from microbit import sleep, pin12
import neopixel

np = neopixel.NeoPixel(pin12, 4)
while True:
    for i in range(4):
        np[i] = (255, 0, 0)
        np.show()
        sleep(100)
        np.clear()
