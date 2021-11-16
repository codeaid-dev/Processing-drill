x,y = [],[]
s = 50
atari = 0
hit = False
r,g,b = random(256),random(256),random(256)
def setup():
    global x,y,atari
    size(500,500)
    for i in range(100):
        x.append(i%10*s)
        y.append(i/10*s)
        #y.append(i//10*s)
    atari = int(random(100))

def draw():
    background(r,g,b)
    for i in range(len(x)):
        if i == atari and hit:
            fill(255,0,0)
        elif i == atari:
            fill(255,250)
        else:
            fill(255)
        rect(x[i],y[i],s,s)

def mousePressed():
    global hit
    for i in range(len(x)):
        if x[i] < mouseX and x[i]+s > mouseX and \
            y[i] < mouseY and y[i]+s > mouseY and \
                i == atari:
            hit = True
