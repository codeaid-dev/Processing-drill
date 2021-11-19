float x = 250;
float y = 250;
float dx = 1;
float dy = 2;
float s = 50;
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    if (mousePressed) {
        fill(255,0,0);
        s = 100;
    } else {
        fill(0);
        s = 50;
    }
    ellipse(x, y, s, s);
    x += dx;
    y += dy;
    if (y-s/2 < 0 || y+s/2 > height) {
        dy *= -1;
    }
    if (x-s/2 < 0 || x+s/2 > width) {
        dx *= -1;
    }
}
