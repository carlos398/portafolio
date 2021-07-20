""" 
    Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

"""


def mayor_o_no():
    print("Es usted mayor de edad?")
    edad = int(input("Digite su edad: "))
    if edad >= 18:
        print("Felicidades es mayor de edad")
    else:
        print("lo sentimos no es mayor de edad")


"""
    Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
    pregunte al usuario por la contraseña e imprima por pantalla
    si la contraseña introducida por el usuario coincide con la guardada en la variable
    sin tener en cuenta mayúsculas y minúsculas.
"""


def contraseña():
    contraseña = input("Digite una contraseña: ")
    contraseña = contraseña.upper()
    confirmacion_contraseña = input("Por favor confirme su contraseña: ")
    confirmacion_contraseña.upper()
    if confirmacion_contraseña == contraseña:
        print("Perfecto las contraseñas coinciden ")
    else:
        contraseña()
   

"""

    Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
    Si el divisor es cero el programa debe mostrar un error.

"""


def division():
    num1 = int(input("Digite un numero para dividir: "))
    num2 = int(input("Digite otro numero para dividir con el primero: "))
    if num2 == 0:
        print("error no se puede dividir entre 0")
    else:
        print(' {0} '.format(( num1 / num2 )))


"""
    Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""


def par_impar():
    numero = int(input('Por favor digite un numero para saber si es par o no: '))
    if numero % 2 != 0:
        print("el numero no es par")
    else:
        print("el numero es par")


if __name__ == '__main__':
    par_impar()