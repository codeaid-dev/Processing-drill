float x = 250;
float y = 250;
float dx = 1;
float dy = 2;
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    ellipse(x, y, 50, 50);
    x += dx;
    y += dy;
    if (y-25 < 0 || y+25 > height) {
        dy *= -1;
    }
    if (x-25 < 0 || x+25 > width) {
        dx *= -1;
    }
}
