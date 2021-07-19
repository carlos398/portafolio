"""

documentacion para el uso de apertura de archivos
r -> Solo lectura
r+ -> Lectura y escritura
w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
a -> Añadido (agregar contenido). Crea el archivo si éste no existe
a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.
las funciones de orden superior reciben otra funcion como parametro
las funciones anonima solo reciben un parametro

with open ("./ruta/del/archivo.formato", "r") as f:   <---- codigo para abrir la f es como nos vamos a referir a el

"""


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r") as f: 
        for line in f:
            numbers.append(int(line))
            numero = int(line)
            if numero == 54:
                print(f'el {numero} encontrado')
    print(numbers)


def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose"]
    with open("./archivos/names.txt", "a") as f:
        for name in names: 
            f.write(name)
            f.write("\n")
        


def run():
    read()


if __name__ == '__main__':
    run()