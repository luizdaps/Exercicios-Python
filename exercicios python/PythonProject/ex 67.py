n = s = 1
while True:
    n = int(input('quer ver a tabuada de qual valor?:'))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{c}x{n} = {c * n}')



