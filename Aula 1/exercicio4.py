tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = tamanho / 3.0
latas = int(litros / 18.0)

##A quantidade de litros a serem utilizados pode ser maior
# que a quantidade de litros inteiros calculados na variável lata
# portanto abaixo é adicionada uma lata caso o resto da divisão
# entre lata e litros seja diferente de zero
if (litros % 18 != 0):
    latas += 1

print(f'Voce devera comprar {latas} latas.')
print(f'O custo total das tintas é R$ {float(latas * 80)}')
