'''
1. Elabore um programa que leia um número, e se ele for maior do que 20, 
escreva a metade desse número, caso contrário escreva o próprio número.
'''

print('Digite um numero:')
numero = float(input())
if(numero>20):
    print(numero/2)
else:
    print(numero)