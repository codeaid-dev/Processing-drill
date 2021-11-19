float x = 250;
float y = 250;
float dx = 1;
float dy = 2;
boolean status = true;
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    if (y-25 < 0 || y+25 > height) {
        dy *= -1;
    }
    if (x-25 < 0 || x+25 > width) {
        dx *= -1;
    }
    if (status) {
        x += dx;
        y += dy;
    }
    ellipse(x, y, 50, 50);
}

void mouseClicked() {
    if (status) {
        status = false;
    } else {
        status = true;
    }
}
