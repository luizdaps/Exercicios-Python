from ex108 import moeda

p = float(input('degite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'aumentar o preço em 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')