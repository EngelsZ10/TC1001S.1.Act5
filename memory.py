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
end = False
change_tiles = False
colores = ['#FFFFFF', '#000000', '#006400',  '#8B0000', '#0000CD', 
	   '#4B0082', '#191970', '#FF0000', '#8B4513', '#2F4F4F',
	   '#DC143C', '#FF4500', '#C71585', '#9400D3', '#008B8B',
	   '#6B8E23', '#696969', '#B8860B', '#FF1493', '#CD5C5C',
	   '#CC6666', '#00FF00', '#6A5ACD', '#FF8C00', '#FF6347',
	   '#00FFFF', '#FFFF00', '#FFC0CB', '#98FB98', '#FFD700',
	   '#66CDAA', '#DEB887', 'blue']

def square(x, y, txt):
    "Draw white square with black outline at (x, y)."
    global change_tiles
    up()
    goto(x, y)
    down()
    color('black', txt)
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
    global end
    spot = index(x, y)
    mark = state['mark']

    if y<168:
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
            if not end:
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
    global end
    clear()
    goto(0, -30)
    shape(car)
    if True not in hide:
        end = True
        text = "gg ganaste con " + str(click_count) + " intentos"  
    else:
        text = "numero de intentos: "+ str(click_count) 
    stamp()
    penup()
    goto(-197, 173)
    pendown()
    color('black','white')
    begin_fill()

    for count in range(2):
        forward(320)
        left(90)
        forward(60)
        left(90)
    
    penup()
    goto(125, 173)
    pendown()
    
    for count in range(2):
        forward(60)
        left(90)
        forward(60)
        left(90)

    end_fill()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count) 
            square(x, y, 'white')

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        square(x, y, colores[tiles[mark]])
        up()
        goto(x + 27, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')
    
    penup()
    goto(-35, 190)
    pendown()
    write(text, font=('Arial', 18, 'normal'), align='center')
    penup()
    goto(157, 177)
    pendown()
    write("click me \nto add \ncolor", font=('Arial', 10, 'normal'), align='center')

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
