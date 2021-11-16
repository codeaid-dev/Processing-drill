def setup():
    size(500, 500)
    background(255)

def draw():
    pass

def mouseClicked():
    drawTree(mouseX, mouseY)

def drawTree(x, y):
    noStroke()
    fill(0,100,0)
    triangle(x,y,x-20,y+20,x+20,y+20)
    triangle(x,y+20,x-40,y+40,x+40,y+40)
    triangle(x,y+40,x-60,y+60,x+60,y+60)
    fill(100,64,0)
    rect(x-10,y+60,20,40)
