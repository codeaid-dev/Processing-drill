x,y = [],[]
s = 50
def setup():
    global x,y
    size(500,500)
    for i in range(100):
        x.append(i%10*s)
        y.append(i/10*s)
        #y.append(i//10*s)

def draw():
    background(255)
    for i in range(len(x)):
        rect(x[i],y[i],s,s)
