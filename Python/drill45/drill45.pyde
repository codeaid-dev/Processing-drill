x,y = [],[]
s = 50
atari = []
hit = []
r,g,b = random(256),random(256),random(256)
def setup():
    global x,y,atari
    size(500,500)
    for i in range(100):
        x.append(i%10*s)
        y.append(i/10*s)
        #y.append(i//10*s)
        hit.append(False)
    
    while len(atari) < 5:
        n = int(random(100))
        if n in atari:
            continue
        atari.append(n)

def draw():
    background(r,g,b)
    for i in range(len(x)):
        for a in atari:
            if i == a and hit[i]:
                fill(255,0,0)
                break
            elif i == a:
                fill(255,250)
                break
            else:
                fill(255)
        rect(x[i],y[i],s,s)

def mousePressed():
    global hit
    for i in range(len(x)):
        if x[i] < mouseX and x[i]+s > mouseX and \
            y[i] < mouseY and y[i]+s > mouseY:
                for a in atari:
                    if i == a:
                        hit[i] = True
                        break
