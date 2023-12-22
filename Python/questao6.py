# 6. Faça um programa que peça dois valores inteiros entre 2 e 15 ao usuário e apresente
# todos os valores entre 1 e 1000 que são simultaneamente divisíveis por ambos os
# valores fornecidos pelo usuário.

while True:
    val1 = int(input("Digite um número inteiro entre 2 e 15: "))
    val2 = int(input("Digite um número inteiro entre 2 e 15: "))

    if 2 <= val1 <= 15 and 2 <= val2 <= 15:
        break
    else:
        print("Apenas valores entre 2 e 15 são permitidos!")

print(f"Números divisíveis por {val1} e {val2} entre 1 e 1000:")
for numero in range(1, 1001):
    if numero % val1 == 0 and numero % val2 == 0:
        print(numero)
