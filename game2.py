import pgzrun
from pgzero.actor import Actor
import pylance
import pygame

# Window Size
WIDTH = 800
HEIGHT = 600

# Actors
ash = Actor("ash")
pikachu = Actor("pikachu")

# Setting Initial Positions
ash.pos = (100, 300)
pikachu.pos = (650, 300)

# Draw Everything
def draw():
    screen.clear()
    screen.fill("green")
    ash.draw()
    pikachu.draw()

# Keyboard Controls
def update():
    if keyboard.left:
        ash.x-=5
    if keyboard.right:
        ash.x+=5
    if keyboard.up:
        ash.y+=5
    if keyboard.down:
        ash.y-=5
    if ash.colliderect("pikachu"):
        screen.draw.text("Ash reached Pikachu!", center = (WIDTH//2, 50), fontsize = 40, color = "red")

# Start
pgzrun.go()