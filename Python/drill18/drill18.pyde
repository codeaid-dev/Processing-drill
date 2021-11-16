x = 250
y = 250
speed = 1
ob1_x = 250
ob1_y = 125
ob2_x = 250
ob2_y = 375
def setup():
    size(500,500)

def draw():
    global x,y, speed
    background(255)
    fill(0)
    ellipse(x, y, 50, 50)
    fill(255,0,0)
    ellipse(ob1_x, ob1_y, 100, 100)
    ellipse(ob2_x, ob2_y, 100, 100)
    if keyPressed:
        if keyCode == UP and y-25 > 0:
            dst1 = dist(x, y-speed, ob1_x, ob1_y)
            dst2 = dist(x, y-speed, ob2_x, ob2_y)
            if dst1 > 75 and dst2 > 75:
                y -= speed
        if keyCode == DOWN and y+25 < height:
            dst1 = dist(x, y+speed, ob1_x, ob1_y)
            dst2 = dist(x, y+speed, ob2_x, ob2_y)
            if dst1 > 75 and dst2 > 75:
                y += speed
        if keyCode == LEFT and x-25 > 0:
            dst1 = dist(x-speed, y, ob1_x, ob1_y)
            dst2 = dist(x-speed, y, ob2_x, ob2_y)
            if dst1 > 75 and dst2 > 75:
                x -= speed
        if keyCode == RIGHT and x+25 < width:
            dst1 = dist(x+speed, y, ob1_x, ob1_y)
            dst2 = dist(x+speed, y, ob2_x, ob2_y)
            if dst1 > 75 and dst2 > 75:
                x += speed
