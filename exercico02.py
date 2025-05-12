numero_secreto = 7
tentativas = 0
limite_tentativas = 5

while tentativas < limite_tentativas:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")

if palpite != numero_secreto:
    print("Suas tentativas acabaram. O número era", numero_secreto)