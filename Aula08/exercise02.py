'''
2ª Questão: 
Faça um programa em Python que leia um vetor A de 100 elementos inteiros e diferentes. 
Depois disso, colocar o maior elemento em uma variável chamada Maior e o menor elemento 
em uma variável chamada Menor, mostrando-as em seguida. Calcule e mostre, também, 
a quantidade de pares e a quantidade de ímpares.
'''

A= []
c=0
par = 0
impar = 0
soma = 0
maior = 0
menor = 9999999999999999999
 
for c in range (0,100,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    if num % 2 ==0:
        par = par + 1
    elif num % 2 !=0:
        impar = impar + 1
    c = c + 1

maior = max(A)
menor = min(A)

print ('O maior valor é: ', maior)
print ('O menor valor é: ', menor)
print ('A quantidade de pares é: ', par)
print ('A quantidade de ímpares é: ', impar)