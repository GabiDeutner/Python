'''

3. Faça um programa para receber um valor e escrever se é “positivo” ou “negativo” 
(considere o valor zero como positivo).

'''

def calcular(n1):
    num1 = float(n1)
    if num1 >= 0:
        resultado= 'positivo'
    elif num1 < 0:
        resultado= 'negativo'
    return resultado


numero1= input('Digite um número: ')
result = calcular(numero1)
print('o valor é:',result)