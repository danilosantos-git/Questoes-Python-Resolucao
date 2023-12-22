# 1. Usando if-elif-else, faça um programa que, dependendo da nacionalidade do usuário,
# imprima (br-bom dia; es-buen dia; fr-bom jour; ge-gutten morgen; outros-good
# morning).

nacionalidade = input("Informe a sua nacionalidade: ")

if nacionalidade == 'br':
    print("Bom dia!")
elif nacionalidade == 'es':
    print("Buen día!")
elif nacionalidade == 'fr':
    print("Bonjour!")
elif nacionalidade == 'ge':
    print("Guten Morgen!")
else:
    print("Good morning!")
