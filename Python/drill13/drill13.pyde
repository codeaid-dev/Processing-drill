def setup():
    size(500,500)
    strokeWeight(5)

def draw():
    if mousePressed:
        line(mouseX, mouseY, pmouseX, pmouseY)
