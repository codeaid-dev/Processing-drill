def setup():
    size(500,500)

def draw():
    background(200)
    s = 52
    m = 40
    for y in range(5):
        for x in range(5):
            if y % 2 == 0 and x % 2 == 1:
                fill(255,0,0)
            elif y % 2 == 1 and x % 2 == 0:
                fill(255,0,0)
            else:
                fill(255)
            rect(x*(s+m)+m,y*(s+m)+m,s,s)
