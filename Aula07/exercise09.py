'''

9. Faça um programa que leia três valores 
(considere que não serão informados valores iguais) e apresente o maior deles.

'''

def calcular(n1,n2,n3):
    num1 = float(n1)
    num2 = float(n2)
    num3 = float(n3)
    resultado = max(num1,num2,num3)
    return resultado


numero1= input('Digite um valor: ')
numero2= input('Digite outro valor: ')
numero3= input('Digite outro valor: ')
result = calcular(numero1,numero2,numero3)
print('o maior valor é:',result)