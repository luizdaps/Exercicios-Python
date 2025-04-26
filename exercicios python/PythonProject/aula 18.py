#teste = list()
#teste.append('gutavo')
#teste.append(40)
#galera = list()
#galera.append(teste [:])
#teste[0] = 'maria'
#teste [1] = 22
#galera.append(teste[:])
#print(galera)



#galera = [['joao',19]], ['ana', 33], ['joaoquim',13], ['maria', 45]
#for p in galera:
    #print(f'{p[0]} tem {p[1]} anos de idade')



galera = list()
dado= list()
totmai = totmen =  0
for c in range (0, 3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai+= 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f'temos {totmai} maiores e {totmen} menores  de idade')
