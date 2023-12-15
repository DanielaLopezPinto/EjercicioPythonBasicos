
#Crear los 10 numeros random 
from random import randint
numeros=[randint(1,10)for i in range(0,10)]

print("Lista original")
print(numeros)
print("Lista ordenada ascendente")
numeros.sort() #para organizar la lista de menor a mayor
print(numeros)
print("Lista ordenada scendente")
numeros.sort(reverse=True) #y el reverse modifica a sort 
print(numeros)             #y hace que se organicen de menor a mayor








