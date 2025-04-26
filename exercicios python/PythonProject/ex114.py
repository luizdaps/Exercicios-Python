import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('o site pudim nao esta acessivel no momento')
else:
    print('consegui acessar o site pudim com sucesso')
