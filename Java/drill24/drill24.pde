void setup() {
    size(500,500);
}

void draw() {
    background(200);
    float s = 52;
    float m = 40;
    for (int y=0; y<5; y++) {
      for (int x=0; x<5; x++) {
            if (y % 2 == 0 && x % 2 == 1) {
                fill(255,0,0);
            } else if (y % 2 == 1 && x % 2 == 0) {
                fill(255,0,0);
            } else {
                fill(255);
            }
            rect(x*(s+m)+m,y*(s+m)+m,s,s);
      }
    }
}
