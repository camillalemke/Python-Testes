# Criar um programa que leia o preço de um produto e depois mostre o novo preço com desconto de 5%

preco = float(input('Digite preço R$: '))
novo = preco * 5/100
print('Preco do produto é R$ {}, com desconto de 5% ficou R$ {} '.format(preco, novo))
