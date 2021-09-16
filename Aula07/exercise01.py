'''

1. Elabore um programa que leia um número, e se ele for maior do que 20, escreva a metade desse número, 
caso contrário escreva o próprio número.

'''

def calcular_metade(n):
    num = float(n)
    if num > 20:
        resultado=num/2
    else:
        resultado=num
    return resultado


numero= input('Digite um número: ')
result = calcular_metade(numero)
print('o valor é:',result)