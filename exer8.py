numero = int(input("Digite um número para ver a tabuada (1 a 10): "))
print(f"\nTabuada do {numero} usando for:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")