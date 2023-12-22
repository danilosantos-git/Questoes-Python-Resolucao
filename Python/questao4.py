# 4. Usando um laço while, imprima cada elemento da lista [10,20,30,40,50,60] na ordem
# inversa. Assuma que o número de elementos da lista é desconhecido, dessa forma, use
# a função len para saber o tamanho da lista.

lista = [10, 20, 30, 40, 50, 60]

tamanho_lista = len(lista)

invert_lista = tamanho_lista - 1
while invert_lista >= 0:
    print(lista[invert_lista])
    invert_lista = invert_lista - 1
