float s = 40;
void setup() {
    size(500, 500);
}

void draw() {
  for (int x=0; x<11; x++) {
    for (int y=0; y<11; y++) {
      if (x*s+50==250 || y*s+50==250) {
          fill(0);
      } else if (mouseX > x*s+30 && mouseX < x*s+70 && mouseY > y*s+30 && mouseY < y*s+70) {
          fill(255,0,0);
      } else {
          fill(255);
      }
      ellipse(x*s+50,y*s+50,s,s);
    }
  }
}
