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


if __name__ == '__main__':
    inversiones()