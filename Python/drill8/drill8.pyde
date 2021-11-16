x = 250
y = 250
dx = 1
dy = 2
def setup():
    size(500,500)
    fill(0)
    noStroke()

def draw():
    global x,y, dx,dy
    background(255)
    ellipse(x, y, 50, 50)
    x += dx
    y += dy
    if y-25 < 0 or y+25 > height:
        fill(random(255),random(255),random(255))
        dy *= -1
    if x-25 < 0 or x+25 > width:
        fill(random(255),random(255),random(255))
        dx *= -1
