#maiusculas e minusculas
#simbolos e espaços

"""
Security = chave
5ecurit1 = senha

"""

chave = input("Digite a base da sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "11"
    elif letra in "Cc": senha = senha + "12"
    elif letra in "Dd": senha = senha + "13"
    elif letra in "Ee": senha = senha + "14"
    elif letra in "Rr": senha = senha + "#"  
    elif letra in "Ss": senha = senha + "%"           
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra

    print(senha)


        