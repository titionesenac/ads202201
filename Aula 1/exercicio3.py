altura = (input('Informe a altura: '))

print(f'O peso ideal para a altura {altura} é {72.7 * float(altura.replace(",", ".", )) - 58:.2f}')
