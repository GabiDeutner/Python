'''

Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem 
que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

'''
print('Digite o ano de nascimento:')
numero1 = float(input())
print('Digite o ano atual:')
numero2 = float(input())
idade = numero2-numero1
if(idade>=16):
    print('Você pode votar!')
else:
    print('Você não pode votar!')