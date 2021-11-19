float x = 250;
float y = 250;
float speed = 1;
float ob1_x = 250;
float ob1_y = 125;
float ob2_x = 250;
float ob2_y = 375;
void setup() {
    size(500,500);
}

void draw() {
    background(255);
    fill(0);
    ellipse(x, y, 50, 50);
    fill(255,0,0);
    ellipse(ob1_x, ob1_y, 100, 100);
    ellipse(ob2_x, ob2_y, 100, 100);
    if (keyPressed) {
        if (keyCode == UP && y-25 > 0) {
            float dst1 = dist(x, y-speed, ob1_x, ob1_y);
            float dst2 = dist(x, y-speed, ob2_x, ob2_y);
            if (dst1 > 75 && dst2 > 75) {
                y -= speed;
            }
        }
        if (keyCode == DOWN && y+25 < height) {
            float dst1 = dist(x, y+speed, ob1_x, ob1_y);
            float dst2 = dist(x, y+speed, ob2_x, ob2_y);
            if (dst1 > 75 && dst2 > 75) {
                y += speed;
            }
        }
        if (keyCode == LEFT && x-25 > 0) {
            float dst1 = dist(x-speed, y, ob1_x, ob1_y);
            float dst2 = dist(x-speed, y, ob2_x, ob2_y);
            if (dst1 > 75 && dst2 > 75) {
                x -= speed;
            }
        }
        if (keyCode == RIGHT && x+25 < width) {
            float dst1 = dist(x+speed, y, ob1_x, ob1_y);
            float dst2 = dist(x+speed, y, ob2_x, ob2_y);
            if (dst1 > 75 && dst2 > 75) {
                x += speed;
            }
        }
    }
}
