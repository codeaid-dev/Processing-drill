x = [125,375,125,375]
y = [125,125,375,375]
dx = []
dy = []
def setup():
    size(500,500)
    for i in range(4):
        dx.append(random(1,2))
        dy.append(random(2,3))

def draw():
    global x,y, dx,dy
    background(255)
    line(250,0,250,500)
    line(0,250,500,250)
    for i in range(4):
        if i == 0:
            fill(255,0,0)
            if x[i]-25 < 0 or x[i]+25 > width/2:
                dx[i] *= -1
            if y[i]-25 < 0 or y[i]+25 > height/2:
                dy[i] *= -1
        elif i == 1:
            fill(0,0,255)
            if x[i]-25 < width/2 or x[i]+25 > width:
                dx[i] *= -1
            if y[i]-25 < 0 or y[i]+25 > height/2:
                dy[i] *= -1
        elif i == 2:
            fill(255,255,0)
            if x[i]-25 < 0 or x[i]+25 > width/2:
                dx[i] *= -1
            if y[i]-25 < height/2 or y[i]+25 > height:
                dy[i] *= -1
        else:
            fill(0,255,0)
            if x[i]-25 < width/2 or x[i]+25 > width:
                dx[i] *= -1
            if y[i]-25 < height/2 or y[i]+25 > height:
                dy[i] *= -1

        x[i] += dx[i]
        y[i] += dy[i]
        ellipse(x[i],y[i],50,50)
        
