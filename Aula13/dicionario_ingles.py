'''

5. Criar um dicionário para traduzir palavras em inglês para Português. 
Para este dicionário, o usuário será responsável pelo cadastro de dez palavras e 
suas respectivas traduções. Após realizada a inserção, deverão ser pedidas as 
palavras a serem traduzidas, sendo mostradas sua tradução. No caso da não existência 
da tradução, uma mensagem deve ser mostrada. O programa termina quando for 
digitada a palavra ***

'''

ingles = []
portugues =[]
num = 0
palavra = ''
ing = '' 
port = '' 
trad = '' 
traducao = '' 
posicao = ''
a = '***'


for num in range (0,10,1):
    print('Digite uma palavra em inglês: ')
    ing = str(input())
    ingles.append(ing)
    print('Digite a tradução em português: ')
    port = str(input())
    portugues.append(port)
    num + 1

while palavra != a :
    print('Digite a palavra em inglês para ser traduzida: ')
    trad = str(input())
    if trad in ingles:
        posicao = ingles.index(trad)
        traducao = portugues[posicao]
        d = {'Palavra em Ingles': trad, 'Traducao em Portugues': traducao}
        for chave in d.keys():
            print(f'{chave} = {d[chave]}')
    else:
        print('Essa palavra não existe no dicionário')
    if trad == a:
        break