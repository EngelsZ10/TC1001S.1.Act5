"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
click_count = 0
change_tiles = False

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 230) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 230

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global click_count
    global change_tiles
    spot = index(x, y)
    mark = state['mark']

    if y<168:
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
            click_count +=1 
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None
    else:
        change_tiles = not change_tiles
def draw():
    "Draw image and tiles."
    global click_count
    clear()
    goto(0, -30)
    shape(car)
    stamp()
    up()
    goto(-197, 173)
    down()
    color('black','white')
    begin_fill()

    for count in range(2):
        forward(240)
        left(90)
        forward(60)
        left(90)
    
    end_fill()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 27, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')
    up()
    goto(-75, 190)
    down()
    write("numero de clicks: "+ str(click_count), font=('Arial', 18, 'normal'), align='center')
     
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 480, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
