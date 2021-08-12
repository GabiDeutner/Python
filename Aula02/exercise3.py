'''

3. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. 
A senha válida é o número 1234. 
Devem ser impressas as seguintes mensagens: ACESSO PERMITIDO caso a senha seja válida. 
ACESSO NEGADO caso a senha seja inválida.

'''
print('Digite o nome de usuário:')
nome = str(input())
print('Digite a senha:')
senha = float(input())
senha_certa = 1234
if(senha == senha_certa):
    print('ACESSO PERMITIDO!')
else:
    print('ACESSO NEGADO!')
