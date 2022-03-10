# Función
## Loop de líneas

def setup():
    size(400, 400);
    background(0);

def draw():
    #background(0);

    fill(0,30);
    noStroke();
    rect(0,0,width,height);

    stroke(255);
    # Perlin noise is a random sequence generator producing a more natural, harmonic succession of numbers than that of the standard random() function
    # Aplica sobre el grosor de las líneas
    strokeWeight(noise(frameCount/20.0)*100);
    line(random(width),random(height),random(width),random(height));