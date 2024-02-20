# Criar um programa que leia a largura e altura de uma parede
# Calcular a área da parede e quantidade de tinta para pintar cada 2 metros quadrados 


larg = float(input('Largura da parede '))
alt = float(input('Altura da parede '))
area = larg * alt
print('A parede tem {} x {} que são iguais a {} '.format(larg, alt, area))
tinta = area / 2
print('A quantidade de tinta para pintar {} m é de {} '.format(tinta))


