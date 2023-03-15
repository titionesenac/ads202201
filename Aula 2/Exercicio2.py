print('Comparação de frases')
frase1 = input('Digite a primeira frase: ')
frase2 = input('Digite a segunda frase: ')

print(f'O tamanho da frase "{frase1}" é de {len(frase1)} caracteres')
print(f'O tamanho da frase "{frase2}" é de {len(frase2)} caracteres')

if (len(frase1) != len(frase2)):
    print('As duas frases sao de tamanhos diferentes e possuem conteudo diferente')
else:
    print('As duas strings tem tamanho igual')
    if (frase1 == frase2):
        print('As duas frases possuem o mesmo conteudo')
    else:
        print('As duas frases possuem conteudo diferente')