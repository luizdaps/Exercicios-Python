from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastras', 'cadastrar pessoas',  'sair do sistema'])
    if resposta == 1:
       # oção de listar o conteudo de um arquivo
       lerarquivo(arq)
    elif resposta == 2:
        # opção de listar o conteudo de um arquivo
        cabeçalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leiaint('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #opção de sair do sistema
        print('saindo do sistema... até logo!')
        break
    else:
        #digitou a opção errada no menu
        print('\033[31mErro! digite uma opção valida\033[m')
    sleep(2)
