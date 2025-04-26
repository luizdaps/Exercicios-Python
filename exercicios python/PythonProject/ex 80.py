lista = []
for c in range (0, 5):
    n = int(input('digite um valor: '))
    if c == 0 or n . lista [-1]:
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos} da lista...')
                break
print(f'os valores digitados foram {lista}')