ArrayList<Float> x = new ArrayList<Float>();
ArrayList<Float> y = new ArrayList<Float>();
ArrayList<Float> dx = new ArrayList<Float>();
ArrayList<Float> dy = new ArrayList<Float>();
float s = 50;
void setup() {
  size(500,500);
}

void draw() {
  background(255);
  for (int i=0; i<x.size(); i++) {
    if (x.get(i)-s/2 < 0 || x.get(i)+s/2 > width) {
      float d = dx.get(i)*-1;
      dx.set(i, d);
    }
    if (y.get(i)-s/2 < 0 || y.get(i)+s/2 > height) {
      float d = dy.get(i)*-1;
      dy.set(i, d);
    }
    x.set(i, x.get(i)+dx.get(i));
    y.set(i, y.get(i)+dy.get(i));
    fill(0);
    ellipse(x.get(i),y.get(i),s,s);
  }
}

void mousePressed() {
  x.add((float)mouseX);
  y.add((float)mouseY);
  dx.add(random(1,5));
  dy.add(random(1,5));
}
