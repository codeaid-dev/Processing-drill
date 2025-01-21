x,y = [],[]
s = 50
atari = []
hit = []
r,g,b = random(256),random(256),random(256)
start_time,end_time = None,None
def setup():
    global atari, start_time
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
    start_time = millis()

def draw():
    global end_time
    background(r,g,b)
    count = 0
    for i in range(len(x)):
        for a in atari:
            if i == a and hit[i]:
                fill(255,0,0)
                count += 1
                break
            elif i == a:
                fill(255,250)
                break
            else:
                fill(255)
        rect(x[i],y[i],s,s)
    if count == 5 and end_time == None:
        end_time = (millis()-start_time)/1000
    if count == 5:
        fill(0)
        textSize(50)
        textAlign(CENTER)
        text("Time: "+str(end_time)+"sec",width/2,height/2)

def mousePressed():
    global hit
    for i in range(len(x)):
        if x[i] < mouseX and x[i]+s > mouseX and \
            y[i] < mouseY and y[i]+s > mouseY:
                for a in atari:
                    if i == a:
                        hit[i] = True
                        break
