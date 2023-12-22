# 5. Usando um laço for, imprima cada elemento da lista [10,20,30,40,50,60] na ordem
# inversa. Assuma que o número de elementos da lista é desconhecido, dessa forma, use
# as funções range (para gerar os índices a serem exibidos) e len para saber o tamanho
# da lista.

lista = [10, 20, 30, 40, 50, 60]

for invert_lista in range(len(lista) - 1, -1, -1):
    print(lista[invert_lista])
