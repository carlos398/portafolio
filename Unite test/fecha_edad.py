import datetime


def fecha_nacimiento():
    cadena = "Digite su fecha de nacimiento en el formato: AÑO/MES/DIA: "
    nacimiento = input(cadena)

    return nacimiento

def edad():
    nacimiento = str(fecha_nacimiento())
    nacimiento = nacimiento[:4]
    fechaActual = datetime.datetime.now()
    fechaActual2 = datetime.datetime.strftime(fechaActual, '%Y/%m/%d')
    fechaActual2 = str(fechaActual2[:4])
    edad = int(fechaActual2) - int(nacimiento)

    return edad


if __name__ == '__main__':
    edad()