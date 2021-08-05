'''
9. Faça um programa que leia três valores (considere que não serão informados valores iguais)
e apresente o maior deles.
'''
print('Digite o valor 1:')
valor1 = float(input())
print('Digite o valor 2:')
valor2 = float(input())
print('Digite o valor 3:')
valor3 = float(input())
if(valor1>valor2) & (valor1>valor3):
    print('o maior valor é')
    print (valor1)
elif(valor2>valor1) & (valor2>valor3): 
    print('o maior valor é')
    print (valor2)
else:
    print('o maior valor é')
    print (valor3)
