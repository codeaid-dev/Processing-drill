float x = 200, y = 250;

void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    for (int i=0; i<3; i++) {
        ellipse(i*50+x, y, 50, 50);
    }
}
