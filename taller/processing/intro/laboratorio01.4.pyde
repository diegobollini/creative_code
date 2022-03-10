# Réplica de laboratorio01.png
# Versión 4


def setup():
    r = 26;
    g = 50;
    b = 117;
    i = 0;
    # Comentar o cambiar la cantidad de cuadros por segundo (default = 60 frames per second.)
    size(1000,400);
    for i in range(0, width):
        i = i + 1;
        r = r - 1;
        g = g - 1;
        b = b - 1;
        stroke(r, g, b);
        line(0, i, width, i); 

