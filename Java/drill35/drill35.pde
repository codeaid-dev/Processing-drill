float[][] x = {{125,125},{375,375},{125,125},{375,375}};
float[][] y = {{125,125},{125,125},{375,375},{375,375}};
float[][] dx = {{1,2},{1,2},{1,2},{1,2}};
float[][] dy = {{2,3},{2,3},{2,3},{2,3}};
void setup() {
    size(500,500);
}

void draw() {
  background(255);
  line(250,0,250,500);
  line(0,250,500,250);
  for (int i=0; i<4; i++) {
    for (int j=0; j<2; j++) {
      if (i == 0) {
          fill(255,0,0);
          if (x[i][j]-25 < 0 || x[i][j]+25 > width/2) {
              dx[i][j] *= -1;
          }
          if (y[i][j]-25 < 0 || y[i][j]+25 > height/2) {
              dy[i][j] *= -1;
          }
      } else if (i == 1) {
          fill(0,0,255);
          if (x[i][j]-25 < width/2 || x[i][j]+25 > width) {
              dx[i][j] *= -1;
          }
          if (y[i][j]-25 < 0 || y[i][j]+25 > height/2) {
              dy[i][j] *= -1;
          }
      } else if (i == 2) {
          fill(255,255,0);
          if (x[i][j]-25 < 0 || x[i][j]+25 > width/2) {
              dx[i][j] *= -1;
          }
          if (y[i][j]-25 < height/2 || y[i][j]+25 > height) {
              dy[i][j] *= -1;
          }
      } else {
          fill(0,255,0);
          if (x[i][j]-25 < width/2 || x[i][j]+25 > width) {
              dx[i][j] *= -1;
          }
          if (y[i][j]-25 < height/2 || y[i][j]+25 > height) {
              dy[i][j] *= -1;
          }
      }

      x[i][j] += dx[i][j];
      y[i][j] += dy[i][j];
      ellipse(x[i][j],y[i][j],50,50);
    }
  }
}
