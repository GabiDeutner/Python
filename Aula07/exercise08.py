'''

8. Faça um programa que receba quatro notas de um aluno, 
calcule e apresente a média aritmética das notas e a mensagem “aprovado” ou “reprovado”, 
considerando, para aprovação, média 8,0.

'''

def calcular(n1,n2,n3,n4):
    num1 = float(n1)
    num2 = float(n2)
    num3 = float(n3)
    num4 = float(n4)
    media = num1+num2+num3+num4/4
    if media >= 8:
        resultado='aprovado'
    elif media < 8:
        resultado='reprovado'
    return resultado


numero1= input('Digite a primeira nota: ')
numero2= input('Digite a segunda nota: ')
numero3= input('Digite a terceira nota: ')
numero4= input('Digite a quarta nota: ')
result = calcular(numero1,numero2,numero3,numero4)
print('o aluno está:',result)