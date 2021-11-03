# Percorrendo os elementos de um Dicionário com a função dict.keys()



print ('Percorrendo os elementos de um Dicionário com a função dict.keys()')

print ('==================================================================')

equipamento = {'CPU': 'Intel', 'RAM': '16Gb', 'SSD': '1T'}



for chave in equipamento.keys():

  print(f'Chave = {chave} e Valor = {equipamento[chave]}')

 

 

 # Percorrendo os elementos de um Dicionário com a função dict.values():



print ('Percorrendo os elementos de um Dicionário com a função dict.values()')

print ('====================================================================')





notas = {'Matemática': 10, 'Português': 10, 'Física': 8}



for valor in notas.values():

    print(f'Valor: {valor}')



   

# Percorrendo as chaves e valores de um Dicionário com a função dict.items():



print('Percorrendo as chaves e valores de um Dicionário com a função dict.items()')

print('==========================================================================')





print(notas.items())



# Podemos acessar essse valores utilizando o loop for, para percorrer esses dados:





for chave, valor in notas.items():

    print(f'Chave = {chave} / Valor = {valor}')