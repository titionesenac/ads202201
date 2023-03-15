quantidade_alunos = 0
while (quantidade_alunos <= 0):
    quantidade_alunos = int(input('Informe a quantidade de turmas: '))
    if (quantidade_alunos <= 0):
        print('A quandidade deve ser maior que 0')

soma_alunos = 0
for i in range(0, quantidade_alunos):
    alunos = -1
    while (alunos < 0) or (alunos > 40):
        alunos = int(input('Informe a quantidade de alunos da turma: '))
        if (alunos < 0) or (alunos > 40):
            print('A turma deve ter no mínimo um aluno e no máximo 40 alunos')
    soma_alunos += alunos

media = soma_alunos / float(quantidade_alunos)

print(f'A média de alunos por turma é {int(media)} alunos')