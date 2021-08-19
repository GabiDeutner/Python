'''
3) Faça um programa em Python para ler dois números inteiros representando um intervalo 
e escrever em ordem crescente todos os números ímpares do intervalo.

'''

print('Digite um numero:')
num1 = int(input())
print('Digite outro numero:')
num2 = int(input())
if(num2>num1):
    for num in range (num1,num2,1):
        if(num != num1 and num % 2 == 1):
            print(num)
else:
    for num in range (num2,num1,1):
        if(num != num1 and num % 2 == 1):
            print(num)

