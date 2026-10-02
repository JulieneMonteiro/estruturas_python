# Loop While

import os
os.system("cls")

    #while False: # Se trocar o false por True, crio um loop infinito
    #    print('Looping')

    #print('\nAcabou!\n')

while True:
    os.system("cls")
    print('''
    1) Estou com fome
    2) Estou com sede
    3) Quero minha mãe

    0) Sair
    ''')

    x = input("Escolha uma opção: ")
    if x == '1' :
        print('\nVá comer!')
        input('\nTecle enter para continuar.')

    elif x == '2' :
        print('\nVá beber água!')
        input('\nTecle enter para continuar.')

    elif x == '3' :
        print('\nEla esta trabalhando!')
        input('\nTecle enter para continuar.')       

    elif x == '0':
        print('\nAcabou a brincadeira!!\n')
        break

    else:
        print('\nNão entendi...')
        input('Tecle enter para continuar.')       
        