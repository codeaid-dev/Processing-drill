def setup():
    size(500,500)
    noStroke()

def draw():
    background(255)
    if mouseX < width/2 and mouseY < height/2:
        fill(255,0,0)
        ellipse(width/4, height/4, 200, 200)
    elif mouseX > width/2 and mouseY < height/2:
        fill(0,255,0)
        ellipse(width/4*3, height/4, 200, 200)
    elif mouseX < width/2 and mouseY > height/2:
        fill(0,0,255)
        ellipse(width/4, height/4*3, 200, 200)
    else:
        fill(255,255,0)
        ellipse(width/4*3, height/4*3, 200, 200)
