

primeiro = int(input('primeiro valor:'))
segundo = int(input('segundo valor:'))
opção = 0
while opção != 5:
   print('''=============================
       [ 1 ]somar
       [ 2 ] mutiplicar
       [ 3 ] maior
       [ 4 ]novos numeros
       [ 5 ] sair do programa''')
   opção = int(input('>>>>>>qual sua opção?:'))
   if opção == 1:
       resultado = primeiro + segundo
       print('a soma dos numeros {}+{} é igual a {}'.format(primeiro, segundo, resultado))
   elif opção == 2:
       resultado = primeiro * segundo
       print('a mutiplicação dos numeros {}x{} é igual a {}'.format(primeiro,segundo, resultado))
   elif opção == 3:
       if primeiro > segundo:
           maior = primeiro
           print('o maior numero entre {} e {} é {}'.format(primeiro, segundo, maior))
       else:
           maior = segundo
           print('o maior numero entre {} e {} é {} '.format(primeiro, segundo, maior))
   elif opção == 4:
       print('informe os valores novamente')
       primeiro = int(input('primeiro valor:'))
       segundo = int(input('segundo valor:'))
   elif opção == 5:
       print('finalizando')
   else:
       print('opção invalida')
print('-=-=' * 10)









