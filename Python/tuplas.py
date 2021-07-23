 
#las listas son utiles por que son dinamicas
#las listas implican mucha memoria eso se soluciona con tuplas
#recorrer for una lista es mas rapida con una tupla
#es rapida por que no es dinamica: INMUTABLE
mi_tupla = (1,2,3,4,5)
mi_tupla.append(5) #genera error
for numero in mi_tupla:
    print(numero)
