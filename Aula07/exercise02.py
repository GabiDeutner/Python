'''

2- Elabore um programa que leia dois valores, calcule e apresente a divisão do maior pelo menor.

'''

def calcular(n1,n2):
    num1 = float(n1)
    num2 = float(n2)
    if num1 > num2:
        resultado=num1/num2
    elif num2 > num1:
        resultado=num2/num1
    return resultado


numero1= input('Digite um número: ')
numero2= input('Digite outro número: ')
result = calcular(numero1,numero2)
print('o valor é:',result)