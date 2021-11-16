x,y = 200,250
dx,dy = 1,2

def setup():
    size(500,500)

def draw():
    global x,y,dx,dy
    background(255)
    if x-25 < 0 or x+125 > width:
        dx *= -1
    if y-25 < 0 or y+25 > height:
        dy *= -1
    x += dx
    y += dy
    fill(0)
    for i in range(3):
        ellipse(i*50+x, y, 50, 50)
