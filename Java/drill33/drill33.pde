float[] x = {125,250,375,125,375};
float[] y = {125,250,125,375,375};
float[] dx = {1,1,1,1,1};
float[] dy = {2,2,2,2,2};
boolean[] status = {true,true,true,true,true};
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    for (int i=0; i<5; i++) {
      if (y[i]-25 < 0 || y[i]+25 > height) {
        dy[i] *= -1;
      }
      if (x[i]-25 < 0 || x[i]+25 > width) {
        dx[i] *= -1;
      }
      if (status[i]) {
        x[i] += dx[i];
        y[i] += dy[i];
      }
      ellipse(x[i], y[i], 50, 50);
    }
}

void mouseClicked() {
  for (int i=0; i<5; i++) {
    float dst = dist(mouseX, mouseY, x[i], y[i]);
    if (dst < 25) {
        if (status[i]) {
            status[i] = false;
        } else {
            status[i] = true;
        }
    }
  }
}
