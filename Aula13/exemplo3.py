'''

Crie um dicionário d e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone e endereço.
Usando d, imprima todos os itens do dicionário no formato chave : valor

'''

print('Digite seu nome: ')
nome = str(input())
print('Digite sua idade: ')
idade = str(input())
print('Digite seu telefone: ')
tel = str(input())
print('Digite seu endereço: ')
end = str(input())

d = {'Nome': nome, 'Idade': idade, 'Telefone': tel, 'Endereço':end}

for chave in d.keys():
  print(f'{chave} = {d[chave]}')
  
  
  