

notas = []
contador = 1

while contador < 5:
    notas.append(float(input(f'Informe a {contador}a nota: ')))
    contador += 1

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)

print(f'A média final é {media:.2f}. A sua maior nota foi {maior_nota:.2f} e a menor foi {menor_nota:.2f}')

if media >= 7:
    print("Aprovado, parabéns!")
else:
    print("Usuário em recuperação")
    notas.append(float(input(f'Informe a nota da recuperação: ')))

    recuperacao = sum(notas) / len(notas)

    if recuperacao >= 5:
        print("Aluno aprovado em recuperação")
    else:
        print("Aluno reprovado.")