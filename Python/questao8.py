# 8. Peça um valor entre 100 e 200 ao usuário e apresente a soma dos valores ímpares de
# 0 até o valor fornecido pelo usuário.

while True:
    num_int = int(input("Digite um número inteiro entre 100 e 200: "))
    if 100 <= num_int <= 200:
        break
    else:
        print("Apenas valores entre 100 e 200 são permitidos!")

soma_impar = 0
for numero in range(num_int + 1):
    if numero % 2 != 0:
        soma_impar = soma_impar + numero

print(f"A soma dos números ímpares de 0 até {num_int} é {soma_impar}.")
