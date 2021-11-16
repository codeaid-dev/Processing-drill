x = 50
dx = 1
def setup():
    size(500,500)

def draw():
    global x,dx
    background(255)
    fill(0)
    ellipse(x, height/2, 50, 50)
    x += dx
    if x+25 > width or x-25 < 0:
        dx *= -1
