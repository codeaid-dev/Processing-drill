float y = 450;
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    ellipse(width/2, y, 50, 50);
    y -= 1;
}
