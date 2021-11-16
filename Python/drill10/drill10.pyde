x = 250
y = 250
dx = 2
dy = 2
def setup():
    size(500,500)
    fill(0)
    noStroke()

def draw():
    global x,y, dx,dy
    background(255)
    ellipse(x, y, 50, 50)
    num = frameCount // 50
    #num = int(frameCount / 50)
    if num % 2 == 0:
        x += dx
    else:
        y += dy
    if y-25 < 0 or y+25 > height:
        fill(random(255),random(255),random(255))
        dy *= -1
    if x-25 < 0 or x+25 > width:
        fill(random(255),random(255),random(255))
        dx *= -1
