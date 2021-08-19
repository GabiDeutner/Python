'''
7) Faça um programa em Python para ler o valor de 15 salários, 
e escreva quais os três maiores valores dos salários lidos.

'''

maior1 = 0
maior2 = 0
maior3 = 0

for salario in range (0,15,1):
    print('Digite o salário:')
    salario = int(input())
    if (salario > maior1):
        maior1 = salario
    elif (salario > maior2) and (maior2 < maior1):
        maior2 = salario
    elif (salario > maior3) and (maior3 < maior2):
        maior3 = salario

print("os três maiores salários foram: ",maior1, ",", maior2, ",", maior3)
