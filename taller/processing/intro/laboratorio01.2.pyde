# Réplica de laboratorio01.png
# Versión 2

# Base
size(1000,400);
#background(149, 221, 125);

# Gradient background
r = 26;
g = 50;
b = 117;

for i in range(0, width):
    i = i + 1;
    r = r - 1;
    g = g - 1;
    b = b - 1;
    stroke(r, g, b);
    line(0, i, width, i);

# Estrellas
for star in range(0,20):
    noStroke();
    circle(random(width), random(100),2);

# Piramides
noFill();
stroke(255, 255, 255)
triangle(120, 220, 260, 220, 190, 110);
triangle(460, 220, 750, 220, 600, 140);
triangle(530, 220, 850, 220, 700, 150);

# Línea horizonte
stroke(0)
fill(255, 255, 255);
rect(0, 220, 1200,220);

# Líneas
for linea in range(0, 14):
    line(140, 220, -1900, 400; 1);
    line(200, 220, -1500, 400);
    line(260, 220, -1100, 400);
    line(320, 220, -700, 400);
    line(380, 220, -300, 400);
    line(440, 220, 100, 400);
    line(500, 220, 500, 400);
    line(560, 220, 900, 400);
    line(620, 220, 1300, 400);
    line(680, 220, 1700, 400);
    line(740, 220, 2100, 400);
    line(800, 220, 2500, 400);
    line(860, 220, 2900, 400);



# Pirámides pequeñas
#triangle(x1, y1, x2, y2, x3, y3);
#stroke(value1, value2, value3, alpha);
stroke(0);
triangle(50, 300, 80, 300, 65, 290);
triangle(150, 380, 180, 380, 165, 370);
triangle(320, 250, 350, 250, 335, 240);
triangle(510, 390, 540, 390, 525, 385);
triangle(600, 350, 630, 350, 615, 340);
triangle(800, 280, 830, 280, 815, 270);