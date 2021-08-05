'''
2. Elabore um programa que leia dois valores, calcule e apresente a divisão do maior pelo menor.
'''
print('Digite o numero 1:')
numero1 = float(input())
print('Digite o numero 2:')
numero2 = float(input())
if(numero1>numero2):
    print(numero1/numero2)
else:
    print(numero2/numero1)
