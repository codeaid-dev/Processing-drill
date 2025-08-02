x, y = 0, 0
radius = 0
circles = []

class Circle:
    pass

def setup():
    size(500, 500)
    fill(0, 255, 0)

def draw():
    background(255)
    for c in circles:
        ellipse(c.x, c.y, c.radius*2, c.radius*2)
    ellipse(x, y, radius*2, radius*2)

def mousePressed():
    global x, y
    x = mouseX
    y = mouseY

def mouseReleased():
    global radius
    c = Circle()
    c.x = x
    c.y = y
    c.radius = radius
    circles.append(c)
    radius = 0

def mouseDragged():
    global radius
    radius = dist(x, y, mouseX, mouseY)
