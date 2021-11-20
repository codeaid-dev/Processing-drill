ArrayList<Float> x = new ArrayList<Float>();
ArrayList<Float> y = new ArrayList<Float>();
ArrayList<Float> dx = new ArrayList<Float>();
ArrayList<Float> dy = new ArrayList<Float>();
int wx=0 ,wy=0;
ArrayList<Float> s = new ArrayList<Float>();
ArrayList<Boolean> ready = new ArrayList<Boolean>();

void setup() {
    size(500, 500);
}

void draw() {
    background(255);
    noStroke();
    fill(0, 255, 0);
    for (int i=0; i<ready.size(); i++) {
        if (ready.get(i)) {
            if (x.get(i)-s.get(i)/2 < 0 || x.get(i)+s.get(i)/2 > width) {
                dx.set(i, dx.get(i)*-1);
            }
            if (y.get(i)-s.get(i)/2 < 0 || y.get(i)+s.get(i)/2 > height) {
                dy.set(i, dy.get(i)*-1);
            }
            x.set(i, x.get(i)+dx.get(i));
            y.set(i, y.get(i)+dy.get(i));
        }
        ellipse(x.get(i), y.get(i), s.get(i), s.get(i));
    }
}

void mousePressed() {
    x.add((float)mouseX);
    y.add((float)mouseY);
    wx = mouseX;
    wy = mouseY;
    dx.add(random(1,4));
    dy.add(random(1,4));
    s.add(0.0);
    ready.add(false);
}

void mouseDragged() {
    float dst = dist(wx, wy, mouseX, mouseY);
    s.set(s.size()-1, dst*2);
}

void mouseReleased() {
    ready.set(ready.size()-1, true);
}
