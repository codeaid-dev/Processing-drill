def setup():
    size(500,500)

def draw():
    background(200)
    s = width/10
    for i in range(100):
        if ((i%10)%2==1 and (i//10)%2==0) or ((i%10)%2==0 and (i//10)%2==1):
            fill(0)
        else:
            fill(255)
#        rect(i%10*50,i//10*50,s,s)
        rect(i/10*50,i%10*50,s,s)
    
'''        
    for y in range(10):
        for x in range(10):
            if y % 2 == 0 and x % 2 == 1:
                fill(0)
            elif y % 2 == 1 and x % 2 == 0:
                fill(0)
            else:
                fill(255)
            rect(x*s,y*s,s,s)
'''
