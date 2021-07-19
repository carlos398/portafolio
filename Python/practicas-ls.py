def run():
    personas = [ 
    ["1098745", "Juan Perez", "juan@gmail.com"],
    ["1589445", "Juan Perez1", "juan@gmail1.com"],
    ["1025845", "Juan Perez2", "juan@gmail2.com"],
    ["1035875", "Juan Perez3", "juan@gmail3.com"]

    ]


    for persona in personas:
        cedula = persona[0]
        nombre = persona[1]
        correo = persona[2]
        print("el usuario {cedula} identificado con cc {nombre} es el duelo del correo electronico {correo}".format(
            cedula=cedula,
            nombre=nombre,
            correo=correo
            ))

    print("x"*100)

    for persona in personas:
        print ("el usuario {cedula} identificado con cc {nombre} es el duelo del correo electronico {correo}.".format(
            cedula=persona[0],
            nombre=persona[1],
            correo=persona[2]
            ))


    personasv2 = [ {
        'cedula': persona[0],
        'nombre': persona[1],
        'correo': persona[2]}
        for persona in personas
        ]

    print("x"*100)

    for persona in personasv2:
        print("el usuario {cedula} identificado con cc {nombre} es el duelo del correo electronico {correo}.".format(**persona))




if __name__ == '__main__':
    run()