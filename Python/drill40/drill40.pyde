x,y = [],[]
dx,dy = [],[]
s = 50
def setup():
    size(500,500)

def draw():
    background(255)
    for i in range(len(x)):
        if x[i]-s/2 < 0 or x[i]+s/2 > width:
            dx[i] *= -1
        if y[i]-s/2 < 0 or y[i]+s/2 > height:
            dy[i] *= -1
        x[i] += dx[i]
        y[i] += dy[i]
        fill(0)
        ellipse(x[i],y[i],s,s)

def mousePressed():
    if mouseButton == LEFT:
        x.append(mouseX)
        y.append(mouseY)
        dx.append(random(1,5))
        dy.append(random(1,5))
    elif mouseButton == RIGHT:
        for i in range(len(x)):
            dst = dist(mouseX,mouseY,x[i],y[i])
            if dst < s/2:
                dx[i] = 0
                dy[i] = 0
