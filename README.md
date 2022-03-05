# creative_code

Archivos, experimentos, pruebas del taller que estoy haciendo con [@unexCoder](https://github.com/unexCoder/Creative-Code-2022).  
En esta [página de la wiki](/creative_code/) hay info más general sobre la disciplina, y en este repositorio voy a ir subiendo lo que vaya creando con cada herramienta.

## Recursos

- [Taller Creative Code 2022](https://github.com/unexCoder/Creative-Code-2022)
- [Creative code with simple programs](https://funprogramming.org/)

## supercollider

- [Web](https://supercollider.github.io/)
- [Doc](https://doc.sccode.org/Tutorials/Getting-Started)
- Instalación (elementaryos, ubuntu): `$ sudo apt instal supercollider`
- Play >> shift enter

## kodelife

- [Web](https://hexler.net/kodelife)
- [Doc](https://hexler.net/kodelife/manual)
- [Download, verificar release](https://hexler.net/pub/kodelife/kodelife-1.0.4.160-linux-x86_64.deb)
- Instalación (revisar release y plataforma): `$ sudo apt install ./kodelife-1.0.4.160-linux-x86_64.deb`
- shaders

## processing

- [Web](https://processing.org)
- [Documentación](https://py.processing.org/tutorials/)
- se recomienda [v3x](https://github.com/processing/processing/releases/download/processing-0270-3.5.4/processing-3.5.4-linux64.tgz) para usar la librería de python

```bash
# Instalar
$ cd processing-3.5.4
$ sudo bash install.sh
```

### processing. notas

- modo dinámico
  - setup (primer función), una vez, definiciones del programa
  - draw, main loop en algunos tutoriales
- stroke= borde de la forma
- color digital en 24 bits
- background(random(255),random(255),random(255));
- funciones de color 1 2 3 4 argumentos
- rojo azul verde transparencia
- coordenadas --> 0 0 (arriba a la izquierda)
- rect(30, 20, 155, 155);
