"""
Beecrowd 1001 - Extremamente Básico

Leia 2 valores inteiros e armazene-os nas variáveis A e B.
Efetue a soma de A e B atribuindo o seu resultado na variável X.
Imprima X conforme exemplo apresentado abaixo.
Não apresente mensagem alguma além daquilo que está sendo especificado e
não esqueça de imprimir o fim de linha após o resultado, caso contrário,
você receberá "Presentation Error".
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1001

# Escreva sua solução abaixo
# Lê os dois valores de entrada (um em cada linha)
a = int(input())
b = int(input())

# Efetua a soma
x = a + b

# Imprime o resultado no formato exato solicitado: "X = [valor]"
# O Python, por padrão, já adiciona o caractere de nova linha (\n) ao final do print
print(f"X = {x}")
