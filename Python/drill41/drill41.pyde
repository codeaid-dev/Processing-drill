x, y = [], []
dx, dy = [], []
wx,wy = 0,0
s = []
ready = []

def setup():
    size(500, 500)

def draw():
    background(255)
    noStroke()
    fill(0, 255, 0)
    for i in range(len(ready)):
        if ready[i]:
            if x[i]-s[i]/2 < 0 or x[i]+s[i]/2 > width:
                dx[i] *= -1
            if y[i]-s[i]/2 < 0 or y[i]+s[i]/2 > height:
                dy[i] *= -1
            x[i] += dx[i]
            y[i] += dy[i]
        ellipse(x[i], y[i], s[i], s[i])

def mousePressed():
    global wx, wy
    x.append(mouseX)
    y.append(mouseY)
    wx = mouseX
    wy = mouseY
    dx.append(random(1,4))
    dy.append(random(1,4))
    s.append(0)
    ready.append(False)

def mouseDragged():
    global s
    dst = dist(wx, wy, mouseX, mouseY)
    s[len(s)-1] = dst*2

def mouseReleased():
    ready[len(ready)-1] = True
