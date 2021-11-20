ArrayList<Float> x = new ArrayList<Float>();
ArrayList<Float> y = new ArrayList<Float>();
float s = 50;
ArrayList<Integer> atari = new ArrayList<Integer>();
ArrayList<Boolean> hit = new ArrayList<Boolean>();
float r = random(256);
float g = random(256);
float b = random(256);
void setup() {
  size(500,500);
  for (int i=0; i<100; i++) {
    x.add(i%10*s);
    y.add(i/10*s);
    hit.add(false);
  }
  while (atari.size() < 5) {
    int n = (int)random(100);
    if (atari.contains(n)) {
      continue;
    }
    atari.add((int)random(100));
  }
}

void draw() {
    background(r,g,b);
  for (int i=0; i<x.size(); i++) {
    for (int a : atari) {
      if (i == a && hit.get(i)) {
        fill(255,0,0);
        break;
      } else if (i == a) {
        fill(255,250);
        break;
      } else {
        fill(255);
      }
    }
    rect(x.get(i),y.get(i),s,s);
  }
}

void mousePressed() {
  for (int i=0; i<x.size(); i++) {
    if (x.get(i) < mouseX && x.get(i)+s > mouseX && 
        y.get(i) < mouseY && y.get(i)+s > mouseY) {
      for (int a : atari) {
        if (i == a) {
          hit.set(i, true);
          break;
        }
      }
    }
  }
}
