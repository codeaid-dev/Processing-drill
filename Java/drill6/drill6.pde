float y = 450;
float dy = 1;
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    ellipse(width/2, y, 50, 50);
    y += dy;
    if (y-25 < 0 || y+25 > height) {
        dy *= -1;
    }
}
