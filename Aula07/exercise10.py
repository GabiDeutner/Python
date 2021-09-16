'''

10. As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, 
e R$ 1,00 se forem compradas pelo menos 12. 
Escreva um programa que leia o número de maçãs compradas, 
calcule e escreva o custo total da compra.

'''

def calcular(n1,v1,v2):
    num1 = float(n1)
    v1 = 1.30
    v2 = 1.00
    if num1 >= 12:
        resultado = num1*v1
    elif num1 < 12:
        resultado = num1*v2
    return resultado


numero1= input('Digite a quantidade de maçãs compradas: ')
valor1 = 1.30
valor2 = 1.00
result = calcular(numero1,valor1,valor2)
print('o custo total da compra é R$:',result, 'reais')