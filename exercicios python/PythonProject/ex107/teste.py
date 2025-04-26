import moeda

p = float(input('degite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'aumentar o preço em 10%, temos R${moeda.aumentar(p, 10)}')