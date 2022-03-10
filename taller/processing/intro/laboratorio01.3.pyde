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
