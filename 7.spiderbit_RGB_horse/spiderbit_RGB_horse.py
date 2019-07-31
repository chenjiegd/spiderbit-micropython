from microbit import sleep, pin12
import neopixel

np = neopixel.NeoPixel(pin12, 4)
a = [0, 1, 2, 3]
b = [1, 2, 3, 0]
c = [2, 3, 0, 1]
d = [3, 0, 1, 2]
s = [a, b, c, d]
while True:
    for i in range(4):
        np[s[i][0]] = (255, 0, 0)
        np[s[i][1]] = (0, 255, 0)
        np[s[i][2]] = (0, 0, 255)
        np[s[i][3]] = (255, 255, 0)
        np.show()
        sleep(500)
