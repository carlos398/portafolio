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
    return True


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
    return True
   

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
    return True


"""
    Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""


def par_impar():
    numero = int(input("Por favor digite un numero para saber si es par o no: "))
    if numero % 2 != 0:
        print("el numero no es par")
    else:
        print("el numero es par")
    return True


"""
    Para tributar un determinado impuesto se debe ser mayor de 16 años 
    y tener unos ingresos iguales o superiores a 1000 € mensuales. 
    Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
    y muestre por pantalla si el usuario tiene que tributar o no.
"""


def impuestos():
    edad = int(input("Por favor digite su edad: "))
    ingresos = int(input("Por favor digite sus ingresos: "))
    print("su edad es {edad} y sus ingresos son {ingresos}€".format(edad=edad, ingresos=ingresos))
    if edad > 16 and ingresos >= 1000:
        print("por tanto usted debe tributar")
    else:
        print("por tanto usted no debe tributar")
    return True


"""
    Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""


def grupos_curso():
    genero = input("Cual es tu genero M = Masculino o F = Femenino: ")
    nombre = input("Cual es tu nombre?: ")
    if (genero == "M" and nombre.lower() > "n") or (genero == "F" and nombre.lower() < "m"):
        print("Grupo A")
    else:
        print("Grupo B")
    return True


"""
    Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
    Renta	Tipo impositivo
    Menos de 10000€	5%
    Entre 10000€ y 20000€	15%
    Entre 20000€ y 35000€	20%
    Entre 35000€ y 60000€	30%
    Más de 60000€	45%
    Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""


def renta_anual(args):
    renta = int(input("Digite su renta anual: "))
    if renta < 10000:
        print("su impositivo es del 5% ")
    elif renta >= 10000 and renta < 20000:
        print("su impositivo es del 15% ")
    elif renta >= 20000 and renta < 35000:
        print("su impositivo es del 20% ")
    elif renta >= 35000 and renta < 60000:
        print("su impositivo es del 30% ")
    else:
        print("su impositivo es del 45% ")
    return True


if __name__ == '__main__':
    grupos_curso()