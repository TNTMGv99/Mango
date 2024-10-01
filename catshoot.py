import pgzrun
import random
WIDTH=500
HEIGHT=500

message = ""

cat=Actor("cat3")


def draw():
    screen.clear()
    screen.fill("blue")
    cat.draw()
    screen.draw.text(message, center = (400, 10), fontsize= 30)

def place_cat():
    cat.x = random.randint(50, WIDTH-50)
    cat.y = random.randint(50, WIDTH-50)


def on_mouse_down(pos):
    global message
    if cat.collidepoint(pos):
      message = "Good shot"
      place_cat()
    else:
      message = "You missed"


place_cat()
pgzrun.go()