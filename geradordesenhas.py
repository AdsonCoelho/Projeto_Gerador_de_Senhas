"""
Criação do meu próprio gerador de senhas em Python

chave = input("Digite a base da sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "1"
    elif letra in "Bb": senha = senha + "@"
    elif letra in "Cc": senha = senha + "2"
    elif letra in "Dd": senha = senha + "3"
    elif letra in "Ee": senha = senha + "4"
    elif letra in "Rr": senha = senha + "#"  
    elif letra in "Ss": senha = senha + "%"           
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra
    print(senha)

"""


import random

min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'

qnt = input('Digite qual tamanho da senha: ')
qntInt = int(qnt)
length = qntInt

#fazendo senha com todos
all = min + max + num + sybs
passwordAll = "".join(random.sample(all, length))

#só maiúsculas e números
MAXnum = max + num
passwordMAXnum = "".join(random.sample(MAXnum, length))

#só minusculas e maiúsculas
MAXmin = max + min
passwordMAXmin = "".join(random.sample(MAXmin, length))

# Executando o código
print('passwordAll = ' + passwordAll) 
print('passwordMAXnum = ' + passwordMAXnum) 
print('passwordMAXmin = ' + passwordMAXmin)
