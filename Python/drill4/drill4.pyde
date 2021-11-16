y = 450
def setup():
    size(500,500)

def draw():
    global y
    background(255)
    fill(0)
    ellipse(width/2, y, 50, 50)
    y -= 1
    if y+25 < 0:
        y = 525
