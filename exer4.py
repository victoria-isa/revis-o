soma = 0
for x in range(0,5):
    num = int(input("digite um número :"))
    soma = soma + num
media = soma/5
print(media)
if media > 7:
    print("aprovado")
elif media <4 :
    print("reprovado")
elif media > 4 and media < 7:
    print("recuperação")
else:
    print("número inválido")

