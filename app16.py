# Loop While

import os
os.system("cls")

while True:
    os.system("cls")
    
    print('\tPaiêêê...')
    print('''
    1) Estou com fome
    2) Estou com sede
    3) Quero minha mãe

    0) Sair
    ''')

    x = input("Escolha uma opção: ")

    match x:
        case '0' :
            print('\nAcabou a brincadeira!!\n')
            break

        case '1':            
            print('\nVá comer!')
        
        case '2' :
            print('\nVá beber água!')
        
        case '3' :
            print('\nTambém quero, mas ela está trabalhando!')
         
        # Nenhuma das opçoes é valida
        case _:
            print('\nNão entendi...')
        
    input('\nTecle [Enter} para continuar.')         