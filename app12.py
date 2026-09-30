import os
os.system('cls')

pessoas = [
    { 'nome': 'Maria', 'idade': 45, 'conceito': 'A' },
    { 'idade': 54, 'nome': 'Joca',  'conceito': 'I'},
    { 'nome': 'Mariana', 'idade': 27, 'conceito': 'A'}
]

contador = 1

for pessoa in pessoas:
    print(
        f'''
{contador}) {pessoa['nome']}:
\t • Idade: {pessoa['idade']}
\t • Conceito: {pessoa['conceito']}
        ''' 
    )
    contador = contador + 1