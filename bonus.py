# ## Desafio
#
# Dados ``n`` pares de parênteses, escreva uma função para gerar todas as combinações de parênteses bem formados.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# n = 3
# ```
#
# A saída deve ser:
#
# ```
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# ```
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def bonus(n):
    if n == 0:
        return []
    elif n == 1:
        return ['()']
    else:
        lista = []
        for i in range(n):
            for j in bonus(i):
                for k in bonus(n-1-i):
                    lista.append('('+j+')'+k)
        return lista

if __name__ == '__main__':
    print(bonus(10))
