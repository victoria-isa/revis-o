contador = 0
for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > 50:
        contador += 1
print(f"\nQuantidade de números maiores que 50: {contador}")