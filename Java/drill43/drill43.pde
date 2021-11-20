ArrayList<Float> x = new ArrayList<Float>();
ArrayList<Float> y = new ArrayList<Float>();
float s = 50;
int atari = 0;
boolean hit = false;
void setup() {
  size(500,500);
  for (int i=0; i<100; i++) {
    x.add(i%10*s);
    y.add(i/10*s);
  }
  atari = (int)random(100);
}

void draw() {
  background(255);
  for (int i=0; i<x.size(); i++) {
    if (i == atari && hit) {
      fill(255,0,0);
    } else {
      fill(255);
    }
    rect(x.get(i),y.get(i),s,s);
  }
}

void mousePressed() {
  for (int i=0; i<x.size(); i++) {
    if (x.get(i) < mouseX && x.get(i)+s > mouseX && 
        y.get(i) < mouseY && y.get(i)+s > mouseY && 
            i == atari) {
        hit = true;
    }
  }
}
