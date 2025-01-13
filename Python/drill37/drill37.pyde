x,y,dx,dy = [],[],[],[]
status = []
interval = []
def setup():
    size(500,500)
    noStroke()
    for i in range(5):
        x.append(random(25,475))
        y.append(random(25,475))
        dx.append(random(1,4))
        dy.append(random(1,4))
        if int(random(2)) == 0:
            status.append(True)
        else:
            status.append(False)
        interval.append(int(random(120,240)))

def draw():
    background(255)
    fill(255,0,0)
    for i in range(5):
        if y[i]-25 < 0 or y[i]+25 > height:
            dy[i] *= -1
        if x[i]-25 < 0 or x[i]+25 > width:
            dx[i] *= -1
        x[i] += dx[i]
        y[i] += dy[i]
        if frameCount % interval[i] == 0:
            status[i] = not status[i]
        if status[i]:
            ellipse(x[i], y[i], 50, 50)
