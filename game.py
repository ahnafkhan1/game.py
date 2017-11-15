import gamebox
import pygame
import random

cam_width, cam_height = 800,600
camera = gamebox.Camera(cam_width,cam_height)

def tick(keys):
    camera.clear("gold")
    instruction_box = gamebox.from_text(400,210,"Welcome to ROADRUNNER'S RAGE!", "arial",25,"black")
    line1 = gamebox.from_text(400,270,"Collect as many crickets as you can before you run out of health.", "arial",24,"black")
    line2 = gamebox.from_text(400,300,"Dodge cacti, coyotes, and cars in this high-speed road run.", "arial",24,"black")
    line3 = gamebox.from_text(400,330,"Increase health by collecting very rare gems.", "arial",24,"black")
    line4 = gamebox.from_text(400,390,"Press SPACEBAR to Start Game -->","arial",24,"black")

    camera.draw(instruction_box)
    camera.draw(line1)
    camera.draw(line2)
    camera.draw(line3)
    camera.draw(line4)
    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second,tick)