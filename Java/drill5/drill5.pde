float x = 50;
float dx = 1;
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    ellipse(x, height/2, 50, 50);
    x += dx;
    if (x+25 > width || x-25 < 0) {
        dx *= -1;
    }
}
