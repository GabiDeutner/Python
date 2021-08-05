'''
10. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, 
e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia
 o número de maçãs compradas, calcule e escreva o custo total da compra.
'''

print('Digite o numero de maçãs compradas:')
numero = int(input())
if(numero>=12):
    custo=numero*1
    print('o custo total da compra é R$', custo, 'reais')
else:
    custo=numero*1.3
    print('o custo total da compra é R$', custo, 'reais')
