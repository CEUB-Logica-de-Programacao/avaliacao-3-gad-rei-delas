# ## Questão 2
#
# Estão testando seus conhecimentos matemáticos. Você irá receber um valor de começo e um valor de fim. Você deve
# encontrar todos os números que são quadrados perfeitos entre esses valores. Um quadrado perfeito é um número inteiro
# que pode ser expresso como o quadrado de outro número inteiro. Por exemplo, 9 é um quadrado perfeito, pois 3² = 9.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# 1 9
# ```
#
# A saída deve ser:
#
# ```
# 1 4 9
# ```
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

import math
def q2(start, end):
    lista = []
    for i in range(start, end+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            lista.append(i)
    return lista

if __name__ == '__main__':
    print(q2(1, 9))
