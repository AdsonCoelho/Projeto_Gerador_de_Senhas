<html>
    <head>
        <title>Running a Python script</title>
        <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        </head>
    <body>
        <py-script>
         
            import random

            min = 'abcdefghijklmnopqrstuvwxyz'
            max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            num = '0123456789'
            sybs = '[]{}()*#;/,-_%'
            
            qnt = input('Digite qual tamanho da senha: ')
            qntInt = int(qnt)
            print(qntInt)
            print(" ")
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
            print('Gerando senhas com: ') 
            print('Todos os caracteres  = ' + passwordAll) 
            print('Maiusculas e numeros = ' + passwordMAXnum) 
            print('Minusculas e maiusculas = ' + passwordMAXmin)
        </py-script>
    </body>
</html>