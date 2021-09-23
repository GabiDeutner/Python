'''
1ª Questão:  
Faça um programa em Python que leia um vetor A de 100 números. 
Depois disso, calcular a média e quantos números estão acima da média. 
Calcule, também, a soma dos elementos do vetor.
'''

A= []
c=0
soma = 0
m = 0 
n=0 

for c in range (0,100,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    c = c + 1
    
soma = sum(A)
med = sum(A)/len(A)

for n in A:
    if n > med:
        m = m + 1

print ('A média é: ', med)
print ('Quantidade de números acima da média: ', m)
print ('A soma dos elementos do vetor é: ', soma)