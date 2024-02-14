import random
n1 = str(input('Nome do aluno '))
n2 = str(input('Nome do segundo aluno '))
n3 = str(input('Nome do terceiro aluno '))
n4 = str(input('Nome quarto aluno '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {} '.format(escolhido))
