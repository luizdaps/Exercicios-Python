expr = str(input('digite a expressao: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len (pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('a sua expressao esta valida')
else:print('a sua expressao esta errada ')