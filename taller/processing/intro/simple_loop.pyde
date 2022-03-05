# App simple con un loop de rectángulos de colores que van apareciendo de manera random, con la chance aplicar distintas transparencias y fondo
def setup():
    # Comentar o cambiar la cantidad de cuadros por segundo (default = 60 frames per second.)
    frameRate(4);
    size(650, 650);
    colorMode(RGB,2);
    background(0);

def draw():
    # Comentando esta línea aplica una sola vez el fondo, por lo que los rectángulos quedan visibles en la pantalla y se van acumulando
    #background(0);
    fill(0,0.1);

    # Esto agrega una forma con una transparencia que se va aplicando sobre los rectángulos
    # https://py.processing.org/reference/ellipse.html
    ellipse(width/2,height/2,width,height);
    
    fill(random(2),random(2),random(2));
    rect(random(width),random(height),100,100);
