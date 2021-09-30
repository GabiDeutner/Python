'''

1ª Questão: 
Faça um programa em Python que leia um vetor A de 6 números. 
Depois disso, calcular a média e quantos números estão acima da média e quantos estão abaixo da média. 
Calcule, também, a soma dos elementos acima da média do vetor.

'''
A= []
c=0
soma = 0
acima = []
abaixo = [] 
n=0
ac = 0
ab = 0

for c in range (0,6,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    c = c + 1
    
soma = sum(A)
med = sum(A)/len(A)

for n in A:
    if n > med:
        acima.append(n)
    elif n < med:
        abaixo.append(n)

ac = len(acima)
ab = len(abaixo)
soma = sum(acima)

print ('A média é: ', med)
print ('Quantidade de números acima da média: ', ac)
print ('Quantidade de números abaixo da média: ', ab)
print ('A soma dos elementos acima da média no vetor é: ', soma)