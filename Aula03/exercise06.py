'''
6) Faça um programa em Python para ler 20 números inteiros, em seguida escrever o menor valor lido 
e quantas vezes este ocorreu nos números lidos.

'''

menor = 99999999999
soma = 0

for num in range (0,20,1):
    print('Digite um numero:')
    num = int(input())
    if (num < menor or num == menor):
        menor = num
        soma = soma + 1

print("o maior número foi: ",menor)
print("este valor ocorreu ",soma, "vezes nos números lidos")