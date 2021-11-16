s = 200
ds = 1

def setup():
    size(500,500)
    noStroke()

def draw():
    global s,ds
    background(255)
    if s > width/2 or s < 1:
        ds *= -1
    s += ds
    if mouseX < width/2 and mouseY < height/2:
        fill(255,0,0)
        ellipse(width/4, height/4, s, s)
    elif mouseX > width/2 and mouseY < height/2:
        fill(0,255,0)
        ellipse(width/4*3, height/4, s, s)
    elif mouseX < width/2 and mouseY > height/2:
        fill(0,0,255)
        ellipse(width/4, height/4*3, s, s)
    else:
        fill(255,255,0)
        ellipse(width/4*3, height/4*3, s, s)
