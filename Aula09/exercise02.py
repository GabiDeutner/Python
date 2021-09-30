'''

2ª Questão: Faça um programa em Python que leia um vetor A de 5 elementos inteiros e diferentes. 
Depois disso, colocar o maior elemento em uma variável chamada Maior e o menor 
elemento em uma variável chamada Menor, mostrando-as em seguida. 
Calcule e mostre, também, a quantidade de positivos  e a quantidade de negativos.

'''
A= []
c=0
positivo = []
negativo = []
Maior = 0
Menor = 9999999999999999999
qpos=0
qneg=0
 
for c in range (0,5,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    if num >= 0:
        positivo.append(num)
    elif num < 0:
        negativo.append(num)
    c = c + 1

Maior = max(A)
Menor = min(A)
qpos=len(positivo)
qneg=len(negativo)

print ('O maior valor é: ', Maior)
print ('O menor valor é: ', Menor)
print ('A quantidade de números positivos é: ', qpos)
print ('A quantidade de números negativos é: ', qneg)