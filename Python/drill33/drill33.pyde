x = [125,250,375,125,375]
y = [125,250,125,375,375]
dx = []
dy = []
status = []
def setup():
    size(500,500)
    for i in range(5):
        dx.append(random(1,3))
        dy.append(random(2,4))
        status.append(True)

def draw():
    background(255)
    fill(0)
    for i in range(5):
        if y[i]-25 < 0 or y[i]+25 > height:
            dy[i] *= -1
        if x[i]-25 < 0 or x[i]+25 > width:
            dx[i] *= -1
        if status[i]:
            x[i] += dx[i]
            y[i] += dy[i]
        ellipse(x[i], y[i], 50, 50)

def mousePressed():
    global status
    for i in range(5):
        dst = dist(mouseX, mouseY, x[i], y[i])
        if dst < 25:
            if status[i]:
                status[i] = False
            else:
                status[i] = True
