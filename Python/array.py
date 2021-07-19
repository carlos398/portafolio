 
numeros = [1,3,6,8,1,9,45,90]
# imprime la posicion 2
print(numeros[2])

# agregar elementos a una lista
numeros.append(10)
print(numeros)

# borrar elementos de una lista
numeros.pop(1)
print(numeros)

# recorrer cada elemento
for i in numeros:
    print(i)

# slice de la posicion 1 al 3
print(numeros[1:3])

# sentido inverso
print(numeros[::-1])

# cantidad de veces que aparece en la lista
print(numeros.count(1))

# limpiar una lista
numeros.clear()
print(numeros)
