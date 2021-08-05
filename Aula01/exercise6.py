'''
6. Elabore um programa que leia um número e, se ele for positivo, 
apresente a metade desse número, caso contrário apresente o número ao quadrado.
'''
print('Digite um numero:')
numero = float(input())
if(numero>=0):
    print('a metade desse número é:')
    print(numero/2)
else:
    print('o número ao quadrado é:')
    print(numero*numero)
