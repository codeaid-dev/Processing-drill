float[] x = {0,0,0,0,0};
float[] y = {0,0,0,0,0};
float[] dx = {0,0,0,0,0};
float[] dy = {0,0,0,0,0};
boolean[] status = {true,true,true,true,true};
int[] interval = {0,0,0,0,0};
void setup() {
  size(500,500);
  noStroke();
  for (int i=0; i<5; i++) {
    x[i] = random(25,475);
    y[i] = random(25,475);
    dx[i] = random(1,4);
    dy[i] = random(1,4);
    if ((int)random(2) == 0) {
        status[i] = true;
    } else {
        status[i] = false;
    }
    interval[i] = (int)random(120,240);
  }
}

void draw() {
  background(255);
  fill(255,0,0);
  for (int i=0; i<5; i++) {
    if (y[i]-25 < 0 || y[i]+25 > height) {
      dy[i] *= -1;
    }
    if (x[i]-25 < 0 || x[i]+25 > width) {
      dx[i] *= -1;
    }
    x[i] += dx[i];
    y[i] += dy[i];
    if (frameCount % interval[i] == 0) {
      status[i] = !status[i];
    }
    if (status[i]) {
      ellipse(x[i], y[i], 50, 50);
    }
  }
}
