lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita' )

for comida in lanche:
    print(f'eu vou comer {comida}')

for cont in range (0, len(lanche)):
    print(f'eu vou comer {lanche} na posição {cont}')

for pos, comida in enumerate (lanche):
    print(f'eu vou comer {lanche} na posição {pos}')
print('eu vou comer pra caramba')