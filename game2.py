import pgzrun
import pgzero.screen

# Window Size
WIDTH = 800
HEIGHT = 600

# Actors
ash1 = Actor("ash", (280, 345))
pikachu1 = Actor("pikachu", (100, 245))

# Draw Everything
def draw():
    screen.clear()
    screen.fill("skyblue")
    ash1.draw()
    pikachu1.draw()

# Keyboard Controls
def update():
    if keyboard.left:
        ash1.x-=5
    if keyboard.right:
        ash1.x+=5
    if keyboard.up:
        ash1.y-=5
    if keyboard.down:
        ash1.y+=5
    if ash1.colliderect(pikachu1):
        print("ash reached the pikachu!")

# Start
pgzrun.go()
