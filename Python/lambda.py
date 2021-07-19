from functools import reduce


palindromo = lambda string: string == string[::-1]

print(palindromo('perro'))


my_lis = [1,4,5,9,8,3,6,19]

odd = list(filter(lambda x: x%2 != 0, my_lis))

print(odd)


squares = list(map(lambda x: x**2, my_lis))

print(squares)


conteo = [2,2,2,2,2]

reducidito = reduce(lambda x, z: x * z, conteo)

print(reducidito)