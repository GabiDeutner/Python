'''

6. Elabore um programa que leia um número e, se ele for positivo, 
apresente a metade desse número, caso contrário apresente o número ao quadrado.

'''

def calcular(n1):
    num1 = float(n1)
    if num1 >= 0:
        resultado=num1/2
    elif num1 < 0:
        resultado=num1*num1
    return resultado


numero1= input('Digite um número: ')
result = calcular(numero1)
print('o valor é:',result)