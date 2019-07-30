from microbit import sleep, pin12
import neopixel

np = neopixel.NeoPixel(pin12, 4)
i = [0, 1, 2, 3]
j = [0, 1, 2, 3]
a = [i, j]
while True:
    for i in range(4):
        for i in range(4):
            np[0] = (255, 0, 0)
            np[1] = (0, 255, 0)
            np[2] = (0, 0, 255)
            np[4] = (255, 255, 0)
    np.show()
    sleep(10)
