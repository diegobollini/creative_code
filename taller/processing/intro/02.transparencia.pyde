# Aplicando el modelo dinámico
## Cambiar transparencia y color de forma al mover el mouse sobre el eje x

def setup():
    size(600,600);

def draw():
    background(0);

    fill(120);
    rect(150,150,300,200);

    fill(180,40,240, map(mouseX,0,width,0,255));
    rect(200,200,300,200);
