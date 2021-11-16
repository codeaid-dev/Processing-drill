x = 250
y = 250
speed = 1
def setup():
    size(500,500)
    fill(0)

def draw():
    global x,y, speed
    background(255)
    ellipse(x, y, 50, 50)
    if keyPressed:
        if keyCode == UP and y-25 > 0:
            y -= speed
        if keyCode == DOWN and y+25 < height:
            y += speed
        if keyCode == LEFT and x-25 > 0:
            x -= speed
        if keyCode == RIGHT and x+25 < width:
            x += speed
