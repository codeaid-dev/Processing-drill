ArrayList<Float> x = new ArrayList<Float>();
ArrayList<Float> y = new ArrayList<Float>();
float s = 50;
void setup() {
    size(500,500);
    for (int i=0; i<100; i++) {
        x.add(i%10*s);
        y.add(i/10*s);
    }
}

void draw() {
    background(255);
    for (int i=0; i<x.size(); i++) {
        rect(x.get(i),y.get(i),s,s);
    }
}
