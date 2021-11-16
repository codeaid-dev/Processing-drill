x = [[125,125],[375,375],[125,125],[375,375]]
y = [[125,125],[125,125],[375,375],[375,375]]
dx = [[1,2],[1,2],[1,2],[1,2]]
dy = [[2,3],[2,3],[2,3],[2,3]]
def setup():
    size(500,500)

def draw():
    global x,y, dx,dy
    background(255)
    line(250,0,250,500)
    line(0,250,500,250)
    for i in range(4):
        for j in range(2):
            if i == 0:
                fill(255,0,0)
                if x[i][j]-25 < 0 or x[i][j]+25 > width/2:
                    dx[i][j] *= -1
                if y[i][j]-25 < 0 or y[i][j]+25 > height/2:
                    dy[i][j] *= -1
            elif i == 1:
                fill(0,0,255)
                if x[i][j]-25 < width/2 or x[i][j]+25 > width:
                    dx[i][j] *= -1
                if y[i][j]-25 < 0 or y[i][j]+25 > height/2:
                    dy[i][j] *= -1
            elif i == 2:
                fill(255,255,0)
                if x[i][j]-25 < 0 or x[i][j]+25 > width/2:
                    dx[i][j] *= -1
                if y[i][j]-25 < height/2 or y[i][j]+25 > height:
                    dy[i][j] *= -1
            else:
                fill(0,255,0)
                if x[i][j]-25 < width/2 or x[i][j]+25 > width:
                    dx[i][j] *= -1
                if y[i][j]-25 < height/2 or y[i][j]+25 > height:
                    dy[i][j] *= -1

            x[i][j] += dx[i][j]
            y[i][j] += dy[i][j]
            ellipse(x[i][j],y[i][j],50,50)
