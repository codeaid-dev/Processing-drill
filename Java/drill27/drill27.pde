float x = 0, y = 0;
float up = 50, bottom = -50;
void setup() {
    size(500,500);
    x = random(width);
    y = random(height);
}

void draw() {
    float dx = random(bottom,up);
    float dy = random(bottom,up);
    while (x+dx < 0 || x+dx > width) {
        dx = random(bottom,up);
    }
    while (y+dy < 0 || y+dy > height) {
        dy = random(bottom,up);
    }
    line(x,y,x+dx,y+dy);
    x += dx;
    y += dy;
}
