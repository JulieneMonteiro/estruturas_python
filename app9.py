import os
os.system('cls')


alunas = [
    ('Maria', '2000-10-14', 'A'),
    ('Joana', '1997-08-10', 'A'),
    ('Pedra', '1990-10-05', 'I'),
    ('Manoela', '1997-06-18', 'a'),
    ('Zuleica', '1981-08-10', 'I'),
    # ...
]

print(f'{alunas[1][0]} nasceu em {alunas[1][1]}')

print(alunas[1][0] + ' nasceu em ' + alunas[1][1]) # esse + chama-se concatenar, juntar strings

print(alunas[1][0],'nasceu em', alunas[1][1])

for aluna in alunas: # No python o dois pontos é sinonimo de identação

    if aluna[2].upper() == 'A': # .upper para converter para maiuscula
        print(f'{aluna[0]} nasceu em {aluna[1]} e tem conceito {aluna[2]}')