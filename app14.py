# Mais testes com 'for in'
import os

os.system("cls")

fruta = 'abacate'

print(len(fruta)) # Mostra a quantidade de caracteres
print()
print(fruta[0]) # Mostra a fruta na posição 0
print()
for letra in fruta:
    print(letra)
print()
numeros = [0, 1, 2, 3]
for num in  numeros:
    print(num)    

print()
for num in range(10): # range mostra a quantidade de numeros solicitada, 
    #lembrando que começa com 0, portanto como cando 10 vai gerar de 0 a 9
    print(num)

