import datetime


def fecha_nacimiento():
    print("por favor digite los 4 digitos del año completos")
    print("ejemplo: 2000, 1994, 1990...etc")
    cadena = "Digite su fecha de nacimiento en el formato: DIA/MES/AÑO: "
    nacimiento = input(cadena)
    nacimiento = nacimiento[-4:]
    nacimiento = int(nacimiento)

    return nacimiento


def edad(nacimiento):
    fechaActual = datetime.datetime.now()
    fechaActual2 = datetime.datetime.strftime(fechaActual, '%d/%m/%Y')
    fechaActual2 = str(fechaActual2[-4:])
    edad = int(fechaActual2) - nacimiento

    return edad


if __name__ == '__main__':
    nacimiento = fecha_nacimiento()
    print(edad(nacimiento))
