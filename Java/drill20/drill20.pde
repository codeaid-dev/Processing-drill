float x = 200, y = 250;
float dx = 1, dy = 2;

void setup() {
    size(500,500);
}

void draw() {
    background(255);
    if (x-25 < 0 || x+125 > width) {
        dx *= -1;
    }
    if (y-25 < 0 || y+25 > height) {
        dy *= -1;
    }
    x += dx;
    y += dy;
    fill(0);
    for (int i=0; i<3; i++) {
        ellipse(i*50+x, y, 50, 50);
    }
}
