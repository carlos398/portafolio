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
    
"""


if __name__ == '__main__':
    cuenta_atras()