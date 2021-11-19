void setup() {
    size(500,500);
    strokeWeight(5);
}

void draw() {
    if (mousePressed) {
        line(mouseX, mouseY, pmouseX, pmouseY);
    }
}
