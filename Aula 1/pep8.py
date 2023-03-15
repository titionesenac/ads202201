import os
import sys
from subprocess import Popen, PIPE
import meupacote.sibling
from meupacote import sibling
from meupacote.sibling import example


# Válido
foo = funcao_qualquer(
    variavel1, variavel2,
    variavel3, variavel4)

# Válido
foo = funcao_qualquer(variavel1, variavel2,
                      variavel3, variavel4)

# Válido
def funcao(variavel1, variavel2,
        variavel3, variavel4):
    pass

# Inválido, não dá pra distinguir a indentação
def funcao(variavel1, variavel2,
    variavel3, variavel4):
    pass

# Inválido, argumentos na segunda linha são proibidos
# se não houver alinhamento vertical.
foo = funcao_qualquer(variavel1, variavel2,
    variavel1, variavel2)



with open("path/to/file/one/file1.txt") as file_one, \
     open("path/to/file/two/file2.txt") as file_two:
    file_two.write(file_one.read())


lucro = (salario_bruto
    + (dividendo - dividendo_qualificado)
    - deducao_ira
    - juros_emprestimo_estudantil
)


# Válido.
compra(hamburguer[0], {ovos: 2})

# Inválido.
compra( hamburguer[ 0 ], { ovos: 2 } )


# Válido
foo = (0,)

# Inválido
bar = (0, )

# Válido
if x == 4: print(x, y); x, y = y, x

# Inválido
if x == 4 : print(x , y) ; x , y = y , x



