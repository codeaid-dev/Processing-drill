float x = 0, y = 0;
float radius = 0;
ArrayList<Circle> circles = new ArrayList<>();

class Circle {
  float x,y;
  float radius;
}

void setup() {
  size(500, 500);
  fill(0, 255, 0);
}

void draw() {
  background(255);
  for (Circle c : circles) {
    ellipse(c.x, c.y, c.radius*2, c.radius*2);
  }
  ellipse(x, y, radius*2, radius*2);
}

void mousePressed() {
  x = mouseX;
  y = mouseY;
}

void mouseReleased() {
  Circle c = new Circle();
  c.x = x;
  c.y = y;
  c.radius = radius;
  circles.add(c);
  radius = 0;
}

void mouseDragged() {
  radius = dist(x, y, mouseX, mouseY);
}
