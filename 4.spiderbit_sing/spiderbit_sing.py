from microbit import button_a
import music

while button_a.is_pressed():
    music.play(music.ODE)