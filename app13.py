# Iterando dicionário
import os
os.system('cls')

prods = {
    "cod": "123abc",
    "name": "Caixa de sapato vazia",
    "fabr": "Caixeiro Viajante",
    "preco": 120.99
}

print(prods)
print()

for prod in prods:
    #print(prod)
    #print(prods[prod])
    print(f' • {prod} - {prods[prod]}')

print()
print('♦ ',prods.keys())
print()
for prod in prods.keys(): #retorna as chaves do dicionário
    print('♣',prod) 

print()
for prod in prods.values(): # Retorna os valores do dicionário
    print('♥ ',prod) # alt + 3 = ♥
print()

print()
print('♦ ',prods.items()) # Retorna uma lista de tuplas
for prod_key, prod_Values in prods.items():
    print(f' ☼ {prod_key.capitalize()} - {prod_Values}') # capitalize deixa a primeira letra maiúscula
print()