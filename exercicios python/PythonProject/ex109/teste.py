from ex109 import moeda

p = float(input('degite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p, True)}')
print(f'aumentando 10%, temos R${moeda.aumentar(p, 10, True)}')
print(f'reduzindo 13%, temos {moeda.diminuir(p,13, True)}')