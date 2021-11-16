x = [125,250,375,125,375]
y = [125,250,125,375,375]
dx = [1,1,1,1,1]
dy = [2,2,2,2,2]
status = [True,True,True,True,True]
def setup():
    size(500,500)

def draw():
    global x,y, dx,dy
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

def mouseClicked():
    global status
    for i in range(5):
        dst = dist(mouseX, mouseY, x[i], y[i])
        if dst < 25:
            if status[i]:
                status[i] = False
            else:
                status[i] = True
