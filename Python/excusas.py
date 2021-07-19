# -- coding: utf-8 --
import random #importacion del modulo random

#arreglos de los cuales tomaremos las palabras para generar nuestra excusa 
introduccion = [

    'perdon, hoy no puedo',
    'te pido mil disculpas', 
    'no sabes lo que me paso', 
    'adivina que:', 
    'no puedo ir porque', 
    'ya se que me vas a reputear pero', 
    'venia pisteando como un campeon y de golpe', 
    'me siento reculpable pero', 
    'lamento muchisimo no poder asistir', 
    'vas a pensar que es una excusa pero'

    ]

chivo_expiatorio = [

    'mi sobrino', 
    'el fantasma de hitler', 
    'el papa francisco', 
    'mi ex ', 'el coro del colegio', 
    'Chiche Gelblung ', 'un payaso triste', 
    'el pibito de karate kid', 
    'el plantel de San Lorenzo', 
    'un match de Tinder'
    
    ]

impedimento = [

    'hizo caca en la cama', 
    'se murio adelante mio', 
    'no para de contarme chistes, no me puedo ir', 
    'tiene un ataque de nervios ', 'me contagio sifilis', 
    'me metio limonada en el tanque de nafta', 
    'me apuñalo', 
    'me econtro la placa de bruxismo', 
    'me robo la bicicleta', 
    'subio mis nudes a instagram'
    
    ]


# funcion para evitar que las frases se repitan
# su parametro es la frase que generaremos en la funcion "excusa"
def existentes(frase):
    #abrimos el archivo donde estaran almacenadas las frases usadas 
    with open("./archivos/excusas.txt", "r") as f: 
        # mostramos la excusa generada
        print('la excusa es: "{frase}" '.format(frase=frase)) 

        #recorremos el archivo de texto en busca de la excusa
        for excusas_existentes in f: 
            excusas_existentes = str(excusas_existentes)

            #si la excusa ya fue usada o generada anteriormente nos devuelve false y cerrara la funcion
            if excusas_existentes == str(frase+"\n"): 
                print("excusa ya usada")
                return False
        
        #si la excusa no ha sido usada la usaremos y la agregaremos al archivo de texto como excusa ya usada
        with open("./archivos/excusas.txt", "a") as f:
            print('muy bien agregando')
            f.write(frase+"\n")
            print('agregado')
            return True


def excusa():#generaremos la excusa de esta forma

    # buscaremos de forma aleatoria cada parte de la excusa con el modulo random 
    # moviendonos entre la longitud del arreglo correspondiente a cada parte de la excusa
    inicio = introduccion[random.randint(0, len(introduccion)-1)] 
    medio = chivo_expiatorio[random.randint(0, len(chivo_expiatorio)-1)]
    final = impedimento[random.randint(0, len(impedimento)-1)]
    #pasamos un .format para unir cada parte de la excusa generada
    frase = '{inicio} {medio} {final}'.format(inicio=inicio, medio=medio, final=final) 
    frase = str(frase)

    #regresanis la excusa generada como "frase"
    return frase 


#funcion para correr nuestro programa
def run():

    #si generamos una excusa que ya fue usada, generaremos mas excusas hasta encontrar una que no haya sido usada
    while existentes(excusa()) != True:
        continue


#funcion para iniciar nuestro programa
if __name__ == '__main__':
    run()