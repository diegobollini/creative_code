# Réplica de laboratorio01.png
# Versión 3
# Simple Linear Gradient 
## The lerpColor() function is useful for interpolating between two colors.

# Constants
Y_AXIS = 1
X_AXIS = 2

# Define colors
b1 = color(255)
b2 = color(0)
c1 = color(204, 102, 0)
c2 = color(0, 102, 153)

size(1000,400);
noLoop();

def Foreground(0,0,0,0,0,0,0):
    setGradient(0, 0, width, 200, c2, c1, X_AXIS);
    setGradient(0, 0, width, 200, c1, c2, Y_AXIS);

def setGradient(x, y, w, h, c1, c2, axis):
    noFill()
    if axis == Y_AXIS:  # Top to bottom gradient;
        for i in range(y, y + h + 1):
            inter = map(i, y, y + h, 0, 1);
            c = lerpColor(c2, c1, inter);
            stroke(c);
            line(x, i, x + w, i);

def stars():
    for star in range(0,20):
        point(random(width), random(100),2);



/* # Piramides
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
line(140, 220, -1900, 400);
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
triangle(800, 280, 830, 280, 815, 270); */