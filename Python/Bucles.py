"""
    Escribir un programa que pregunte al usuario su edad y 
    muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def edades():
    edad = int(input("Digite su edad por favor"))
    anio = 2021 - edad
    for i in range(edad+1):
        print("en el año {0} usted cumplio {edad}, ".format((anio+i), edad=i))



""" 
    Escribir un programa que pida al usuario un número entero positivo 
    y muestre por pantalla todos los números impares desde 1 hasta ese número 
    separados por comas.
"""


def impares():
    numero = int(input("Dogite un numero entero positivo: "))
    if numero <=0 :
        print("el numero debe ser entero positivo")
    for i in range(numero+1):
      if i%2:
          print(i, end=", ")



"""
    Escribir un programa que pida al usuario un número entero positivo 
    y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""


def cuenta_atras():
    numero = int(input("Dogite un numero entero positivo: "))
    if numero <=0 :
        print("el numero debe ser entero positivo")
    for i in range(numero+1):
        print(" {0} ".format(numero - i), end=", ")


"""
    Escribir un programa que pregunte al usuario una cantidad a invertir, 
    el interés anual y el número de años, 
    y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""


def inversiones():
    cantidad = int(input("Dogite cuanto quiere invertir: "))
    interes_anual = int(input("el interes anual: "))
    numero_años = int(input("numer de años para la inversion: "))
    for i in range(numero_años):
        cantidad *=  1 + interes_anual / 100
        print(" la ganancia del año {año} es de {ganancia} ".format(año=i+1, ganancia=round(cantidad, 2)))


"""
    Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
    como el de más abajo, de altura el número introducido
"""


def triangulo():
    tamaño = int(input("Digite el tamaño de su triangulo: "))
    for i in range(tamaño):
        print("*"*i)


"""
    Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""


def tabla():
    for i in range(1,11):
        for j in range(1,11):
            print(" {0}".format((i*j)), end='\t')
        print("")


"""
    Escribir un programa que pida al usuario un número entero y 
    muestre por pantalla un triángulo rectángulo como el de más abajo.
"""


def triangulo_nums():
    tamaño = int(input("Digite el tamaño de su triangulo: "))
    for i in range(1, tamaño+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print("")
        

if __name__ == '__main__':
    triangulo_nums()