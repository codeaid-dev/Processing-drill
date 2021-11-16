x = 250
y = 250
dx = 1
dy = 2
status = True
def setup():
    size(500,500)

def draw():
    global x,y, dx,dy
    background(255)
    fill(0)
    if y-25 < 0 or y+25 > height:
        dy *= -1
    if x-25 < 0 or x+25 > width:
        dx *= -1
    if status:
        x += dx
        y += dy
    ellipse(x, y, 50, 50)

def mouseClicked():
    global status
    dst = dist(mouseX, mouseY, x, y)
    if dst < 25:
        if status:
            status = False
        else:
            status = True
