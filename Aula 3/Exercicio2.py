frase = 'Paulo é d4veloper e um b0m musico'
palavras_numeros = []
temp = frase.split()

for palavra in temp:
    for char in palavra:
        if char.isdigit():
            temp.remove(palavra)
            palavras_numeros.append(palavra)
            break

print(f'Palavras com números {" ".join(palavras_numeros)}')
print(f'Frase com as palavras sem números {" ".join(temp)}')