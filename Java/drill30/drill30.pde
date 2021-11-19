float x = 0, y = 0;

void setup() {
    size(500, 500);
    background(255);
    fill(0, 255, 0);
}

void draw() {
}

void mousePressed() {
    x = mouseX;
    y = mouseY;
}

void mouseDragged() {
    float dst = dist(x, y, mouseX, mouseY);
    ellipse(x, y, dst*2, dst*2);
}
