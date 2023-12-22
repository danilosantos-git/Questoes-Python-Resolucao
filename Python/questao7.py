# 7. Peça um valor entre 2 e 20 ao usuário e calcule o fatorial desse número.

while True:
    numero = int(input("Digite um número inteiro entre 2 e 20: "))
    if 2 <= numero <= 20:
        break
    else:
        print("Apenas valores entre 2 e 20 são permitidos!")

fatorial = 1
for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"O fatorial de {numero} é {fatorial}.")
