y = 450
dy = 1
def setup():
    size(500,500)

def draw():
    global y, dy
    background(255)
    fill(0)
    ellipse(width/2, y, 50, 50)
    y += dy
    if y-25 < 0 or y+25 > height:
        dy *= -1
