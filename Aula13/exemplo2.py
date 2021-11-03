'''

Crie um dicionário d e coloque nele seus dados: nome, idade, telefone e endereço.
Usando o dicionário d criado anteriormente, imprima seu nome.

'''


print ('Percorrendo os elementos de um Dicionário com a função dict.keys()')
print ('==================================================================')
gabi = {'Nome': 'Gabriela', 'Idade': '27 anos', 'Telefone': '123456789', 'Endereço':'Rua ABCD número 123'}



for chave in gabi.keys():
  print(f'{chave} = {gabi[chave]}')