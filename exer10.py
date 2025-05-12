frase = input("digite uma frase :")
contador = 0
for letras in frase:
    if letras == "a" or letras =="A":
        contador += 1
print(f"a quantidade de letras A é igual {contador}")
