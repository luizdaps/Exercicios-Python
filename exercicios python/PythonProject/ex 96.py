def area (lar, comp):
    a = lar * comp
    print(f'a area de um terreno {lar}x{comp} é de {a}m².')


#programa principal
print(' controle de terrenos ')
print('-'*20)
l =float(input('largura (m): '))
c = float(input('comprimento (m): '))
area(l, c)