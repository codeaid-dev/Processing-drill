float x = 250;
float y = 250;
float dx = 2;
float dy = 2;
void setup() {
    size(500,500);
    fill(0);
    noStroke();
}

void draw() {
    background(255);
    ellipse(x, y, 50, 50);
    int num = (int)frameCount / 50;
    if (num % 2 == 0) {
        x += dx;
    } else {
        y += dy;
    }
    if (y-25 < 0 || y+25 > height) {
        fill(random(255),random(255),random(255));
        dy *= -1;
    }
    if (x-25 < 0 || x+25 > width) {
        fill(random(255),random(255),random(255));
        dx *= -1;
    }
}
