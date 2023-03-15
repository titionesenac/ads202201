lista_numeros = [414, 267, 411, 1250, 107, 884, 88, 1604, 1153, 287]

for i in lista_numeros:
    if lista_numeros.index(i) % 2 != 0:
        print(f'O número {i} está no índice ímpar {lista_numeros.index(i)}')

