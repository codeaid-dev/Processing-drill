s = 40
def setup():
    size(500, 500)

def draw():
    global s
    for i in range(121):
        if i%11==5 or i//11==5:
            fill(0)
        else:
            fill(255)
        ellipse(i%11*s+50,i//11*s+50,s,s)

'''        
    for x in range(11):
        for y in range(11):
            if x*s+50==250 or y*s+50==250:
                fill(0)
            else:
                fill(255)
            ellipse(x*s+50,y*s+50,s,s)
'''        
