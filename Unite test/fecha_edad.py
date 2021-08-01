import datetime


def edad(nacimiento):
    fechaActual = datetime.datetime.now()
    fechaActual2 = datetime.datetime.strftime(fechaActual, '%Y/%m/%d')
    fechaActual2 = str(fechaActual2[:4])
    edad = int(fechaActual2) - int(nacimiento)

    return edad


cadena = "Digite su fecha de nacimiento en el formato: AÑO/MES/DIA: "
nacimiento = input(cadena)
nacimiento = nacimiento[:4]


if __name__ == '__main__':
    print(edad(nacimiento))