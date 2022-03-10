# Usando imágenes
# Por lo pronto primero hay que agregarlas desde Processing > Sketch > Añadir archivo

def setup():
    frameRate(2);
    smooth();
    global img
    global img2
    size(400, 400);
    # Make a new instance of a PImage by loading an image file
    # Declaring a variable of type PImage
    img = loadImage("vintage-dancers.png")
    img2 = loadImage("vintage-dancers2.png")

def draw():
    background(176,216,116);
    # Draw the image to the screen
    image(img, random(width-80), random(height-80), 110, 110);
    image(img2, random(width-80), random(height-80), 110, 110);