x = 50
def setup():
    size(500,500)

def draw():
    global x
    background(255)
    fill(0)
    ellipse(x, height/2, 50, 50)
    x += 1
    if x-25 > width:
        x = -25
