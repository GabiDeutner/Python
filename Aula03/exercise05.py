'''
5) Faça um programa em Python para ler um valor N e em seguida ler N números inteiros 
e escrever o maior número lido.

'''

maior = 0

print('Digite um numero:')
N = int(input())

for num in range (0,N,1):
    print('Digite um numero:')
    num = int(input())
    if (num > maior):
        maior = num

print("o maior número foi: ",maior)