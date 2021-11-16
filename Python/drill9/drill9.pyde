x = 250
y = 250
dx = 1
dy = 2
s = 50
def setup():
    size(500,500)

def draw():
    global x,y, dx,dy, s,cs
    background(255)
    if mousePressed:
        fill(255,0,0)
        s = 100
    else:
        fill(0)
        s = 50
    ellipse(x, y, s, s)
    x += dx
    y += dy
    if y-s/2 < 0 or y+s/2 > height:
        dy *= -1
    if x-s/2 < 0 or x+s/2 > width:
        dx *= -1
