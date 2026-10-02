# Testes com While e break
import os
os.system('cls')

contador = 1

while contador <= 10:
    print(contador)
    contador = contador +1
    if contador == 6:
        print('Gotcha')
        continue # o continue serve para quando tem mais codigos abaixo, 
    #caso não tenha é desnecessário

    print("PIN")
    