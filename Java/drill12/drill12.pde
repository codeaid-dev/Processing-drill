void setup() {
    size(500,500);
}

void draw() {
    background(255);
    if (mousePressed) {
        fill(255,0,0);
    } else {
        fill(0);
    }
    ellipse(mouseX, mouseY, 50, 50);
}
