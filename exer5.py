senhaValida = "1234"
senha = ""

while senha != senhaValida:
    senha = input("digite a senha ")
    if senha != senhaValida :
        print("senha incorreta")
    else:
        print("senha correta")