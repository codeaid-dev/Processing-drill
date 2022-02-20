//float[] x = {0,0,0,0,0};
//float[] y = {0,0,0,0,0};
//float[] dx = {0,0,0,0,0};
//float[] dy = {0,0,0,0,0};
ArrayList<Float> x = new ArrayList<Float>();
ArrayList<Float> y = new ArrayList<Float>();
ArrayList<Float> dx = new ArrayList<Float>();
ArrayList<Float> dy = new ArrayList<Float>();

boolean status = true;
void setup() {
    size(500,500);
    noStroke();
    for (int i=0; i<5; i++) {
      x.add(random(25,475));
      y.add(random(25,475));
      dx.add(random(1,4));
      dy.add(random(1,4));
//      x[i] = random(25,475);
//      y[i] = random(25,475);
//      dx[i] = random(1,4);
//      dy[i] = random(1,4);
    }
}

void draw() {
    background(255);
    fill(255,0,0);
    if (frameCount % 120 == 0) {
        status = !status;
    }
    for (int i=0; i<5; i++) {
        if (y.get(i)-25 < 0 || y.get(i)+25 > height) {
            dy.set(i, dy.get(i) * -1);
        }
        if (x.get(i)-25 < 0 || x.get(i)+25 > width) {
            dx.set(i, dx.get(i) * -1);
        }
        x.set(i, x.get(i) + dx.get(i));
        y.set(i, y.get(i) + dy.get(i));
        if (status) {
            ellipse(x.get(i), y.get(i), 50, 50);
        }
/*        if (y[i]-25 < 0 || y[i]+25 > height) {
            dy[i] *= -1;
        }
        if (x[i]-25 < 0 || x[i]+25 > width) {
            dx[i] *= -1;
        }
        x[i] += dx[i];
        y[i] += dy[i];
        if (status) {
            ellipse(x[i], y[i], 50, 50);
        }
*/
    }
}
