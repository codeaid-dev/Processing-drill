x,y,dx,dy = [],[],[],[]
status = True
def setup():
    size(500,500)
    noStroke()
    for i in range(5):
        x.append(random(25,475))
        y.append(random(25,475))
        dx.append(random(1,4))
        dy.append(random(1,4))

def draw():
    global x,y, dx,dy, status
    background(255)
    fill(255,0,0)
    if frameCount % 120 == 0:
        status = not status
    for i in range(5):
        if y[i]-25 < 0 or y[i]+25 > height:
            dy[i] *= -1
        if x[i]-25 < 0 or x[i]+25 > width:
            dx[i] *= -1
        x[i] += dx[i]
        y[i] += dy[i]
        if status:
            ellipse(x[i], y[i], 50, 50)
