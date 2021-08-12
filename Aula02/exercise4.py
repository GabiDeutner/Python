'''

4. As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, 
e R$ 0,25 se forem compradas pelo menos doze. 
Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

'''
print('Digite o número de maçãs compradas:')
numero = float(input())
if(numero<12 and numero>0):
    preco = numero * 0.3
    print('O valor total da compra é R$', preco, 'reais')
elif(numero>12 and numero>0):
    preco = numero * 0.25
    print('O valor total da compra é R$', preco, 'reais')
else:
    print('Você não comprou nenhuma maçã')