x,y = 200,250

def setup():
    size(500,500)

def draw():
    background(255)
    fill(0)
    for i in range(3):
        ellipse(i*50+x, y, 50, 50)
