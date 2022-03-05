# COLOR DIGITAL

## Tamaño del marco / app
size(650,650);

# RGB 
## Mezcla de 3 valores llamados "canales" determinando cantidad de luz.
## Red, Green & Blue, donde para cada canal 0 es minima luz y 255 es máxima luz
## https://py.processing.org/reference/background.html
## background(value1, value2, value3, alpha);
background(0,0,0);
background(255,255,255);
background(120,96,167);

# Tonos simples
## Si utilizo un solo valor en funciones que definen color, se obtiene una regla de tonos blanco a negro
## Rectángulo: https://py.processing.org/reference/rect.html
fill(120);
rect(50,50,200,200);
fill(65);
rect(100,100,200,200);

# Transparencia canal alpha
## Un segundo valor a un valor de tono o un cuarto valor a un color en 3 canales, agrega una determinada transparencia
## donde 0 es totalmente transparente y 255 es totalmente opaco

fill(165,100);
rect(150,150,200,200);
fill(255,255,12,120);
rect(200,200,200,200);

# colorMode
## https://py.processing.org/reference/colorMode.html
## For example, calling colorMode(RGB, 1.0) will specify that values are specified between 0 and 1
colorMode(RGB,1,5,12);
fill(0,0,1);
rect(50,500,50,50);
fill(0,1,0);
rect(150,500,50,50);
fill(1,0,0);
rect(250,500,50,50);
fill(1,0,1);
rect(350,500,50,50);
fill(1,1,0);
rect(450,500,50,50);
fill(0,1,1);
rect(550,500,50,50);

# HueSaturationBrightness
colorMode(HSB,200,100,100);
fill(0,100,100);
rect(50,575,50,50);
fill(20,100,100);
rect(150,575,50,50);
fill(40,100,100);
rect(250,575,50,50);
fill(60,100,100);
rect(350,575,50,50);
fill(80,100,100);
rect(450,575,50,50);
fill(100,100,100);
rect(550,575,50,50);
