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
        if keyCode == UP:
            y -= speed
        if keyCode == DOWN:
            y += speed
        if keyCode == LEFT:
            x -= speed
        if keyCode == RIGHT:
            x += speed
