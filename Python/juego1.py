# -- coding: utf-8 --


import random


"""

    Codigo para un juego de busqueda, mostraremos que modo de juego desea,
    puede escoger que combinacion de letras y numeros jugar
    luego le daremos a escoger las dimenciones del tablero, asi mismo
    mostramos letras y numeros similares en una tabla, 
    el usuario debe buscar la ubicacion de dichos numeros similares a las letras

"""


def opciones():
    letra = None
    numero = None
    switch = True #interruptor para ejecutar el bucle while hasta seleccionar una opcion valida
    
    while switch == True:
        modo_de_juego()
        seleccion = int(input("Digite su eleccion: "))

        if seleccion == 0:
            letra = "B"
            numero = 8
            switch = False

        elif seleccion == 1:
            letra = "S"
            numero = 5
            switch = False

        elif seleccion == 2:
            letra = "l"
            numero = 1
            switch = False

        else:   
            print("por favor seleccione una opcion valida")
            switch = True

    mostrar_juego(letra,numero)
    return True


def modo_de_juego(): #seleccionar el modo de juego
    opciones = ["B y 8","S y 5","l y 1"]
    print("*"*10,"Seleccione el tipo de juego","*"*10)

    for contador,valor in enumerate(opciones):
        print("*"*10,"Digite {contador} para jugar {valor} ".format(contador=contador ,valor=valor),"*"*10)
    return True

    # for i in range(len(opciones)):
    #     opcion = opciones[i]
    #     print("*"*10,"Digite {i} para jugar {opcion} ".format(i=i,opcion=opcion),"*"*10)
    # return True


def mostrar_juego(letra, numero): #tiene como parametros una letra y un numero que se usaran para mostrar en el tablero
    horizontal = int(input("Cuantos campos quiere que el juego tenga horizontalmente ?: \n"))
    vertical = int(input("Cuantos campos quiere que el juego tenga verticalmente ?: \n"))
    elementos = [b for b in range(horizontal) ]

    for j in range(vertical):
        
        for i in range(horizontal):
            elementos[i] = " {letra} ".format(letra=letra)
        
        elementos[random.randint(0, len(elementos)-1)] = " {numero} ".format(numero=numero)
        print(j,elementos)    
    return True


def run():
    opciones()


if __name__ == '__main__':
    run()