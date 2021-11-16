x, y = 0, 0

def setup():
    size(500, 500)
    background(255)
    fill(0, 255, 0)

def draw():
    pass

def mousePressed():
    global x, y
    x = mouseX
    y = mouseY

def mouseDragged():
    dst = dist(x, y, mouseX, mouseY)
    ellipse(x, y, dst*2, dst*2)
