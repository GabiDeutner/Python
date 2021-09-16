'''

7. Elabore um programa que leia um valor e escrever
a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, 
caso contrário escrever NÃO É MAIOR QUE 10!

'''

def calcular(n1):
    num1 = float(n1)
    if num1 > 10:
        resultado='É MAIOR QUE 10!'
    elif num1 <= 10:
        resultado='NÃO É MAIOR QUE 10!'
    return resultado


numero1= input('Digite um número: ')
result = calcular(numero1)
print('o valor é:',result)