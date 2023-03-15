lista_numeros = [414, 267, 411, 1250, 107, 884, 88, 1604, 1153, 287]

for i in lista_numeros:
    if i > 1500:
        print(f'O número {i} é maior que 1500, finalizando iteração')
        break
    elif i in range(95, 150):
        print(f'O número {i} entre 95 e 150')
        pass
    elif i % 5 == 0:
        print(f'O número {i} é divsível por 5')
    else:
        print(f'O número {i} não é divisível por 5, não está entre 95 e 150 e não é maior que 1500')

