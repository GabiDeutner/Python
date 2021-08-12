'''

9. Escreva um programa para ler 3 valores inteiros e escrever o maior deles. 
Considere que o usuário não informará valores iguais.

'''
print('Digite o valor 1:')
valor1 = int(input())
print('Digite o valor 2:')
valor2 = int(input())
print('Digite o valor 3:')
valor3 = int(input())
if(valor1>valor2) & (valor1>valor3):
    print('o maior valor é')
    print (valor1)
elif(valor2>valor1) & (valor2>valor3): 
    print('o maior valor é')
    print (valor2)
else:
    print('o maior valor é')
    print (valor3)
