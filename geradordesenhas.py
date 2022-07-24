<html>
    <head>
        <title>Running a Python script</title>
        <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
        <script defer src="https://pyscript.net/alpha/pyscript.js"> </script>
        </head>
    
    <body>
        <py-script>

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

    </py-script>
    </body>
</html>
