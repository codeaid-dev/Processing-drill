float x = 250;
float y = 250;
float speed = 1;
void setup() {
    size(500,500);
    fill(0);
}

void draw() {
    background(255);
    ellipse(x, y, 50, 50);
    if (keyPressed) {
        if (keyCode == UP && y-25 > 0) {
            y -= speed;
        }
        if (keyCode == DOWN && y+25 < height) {
            y += speed;
        }
        if (keyCode == LEFT && x-25 > 0) {
            x -= speed;
        }
        if (keyCode == RIGHT && x+25 < width) {
            x += speed;
        }
    }
}
