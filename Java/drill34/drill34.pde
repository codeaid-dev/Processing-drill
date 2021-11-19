float[] x = {125,375,125,375};
float[] y = {125,125,375,375};
float[] dx = {1,1,1,1};
float[] dy = {2,2,2,2};
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    line(250,0,250,500);
    line(0,250,500,250);
    for (int i=0; i<4; i++) {
        if (i == 0) {
            fill(255,0,0);
            if (x[i]-25 < 0 || x[i]+25 > width/2) {
                dx[i] *= -1;
            }
            if (y[i]-25 < 0 || y[i]+25 > height/2) {
                dy[i] *= -1;
            }
        } else if (i == 1) {
            fill(0,0,255);
            if (x[i]-25 < width/2 || x[i]+25 > width) {
                dx[i] *= -1;
            }
            if (y[i]-25 < 0 || y[i]+25 > height/2) {
                dy[i] *= -1;
            }
        } else if (i == 2) {
            fill(255,255,0);
            if (x[i]-25 < 0 || x[i]+25 > width/2) {
                dx[i] *= -1;
            }
            if (y[i]-25 < height/2 || y[i]+25 > height) {
                dy[i] *= -1;
            }
        } else {
            fill(0,255,0);
            if (x[i]-25 < width/2 || x[i]+25 > width) {
                dx[i] *= -1;
            }
            if (y[i]-25 < height/2 || y[i]+25 > height) {
                dy[i] *= -1;
            }
        }

        x[i] += dx[i];
        y[i] += dy[i];
        ellipse(x[i],y[i],50,50);
    }
}
