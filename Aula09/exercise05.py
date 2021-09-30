'''

 5ª Questão:  Refaça o exercício 2, usando funções. 
 Crie, para isso, as funções MostraMaior, MostraMenor, TotalPositivo e TotalNegativo. 

Faça um programa em Python que leia um vetor A de 5 elementos inteiros e diferentes. 
Depois disso, colocar o maior elemento em uma variável chamada Maior e o menor 
elemento em uma variável chamada Menor, mostrando-as em seguida. 
Calcule e mostre, também, a quantidade de positivos  e a quantidade de negativos.

'''

A= []
listaneg=[]
listapos=[]
c=0
positivo = 0
negativo = 0
soma = 0
total1=0 
total2=0
menor = 99999999999999999
maior=0

for c in range (0,5,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    
def TotalPositivo(A):
    total1 = list(A)
    n1 = 0
    positivo = 0
    for n1 in total1:
        if n1 >= 0:
            listapos.append(n1)
    positivo = len(listapos)
    return positivo
        
def TotalNegativo(A):
    total2 = list(A)
    n2 = 0
    negativo=0
    for n2 in total2:
        if n2 < 0:
            listaneg.append(n2)
    negativo = len(listaneg)
    return negativo

def MostraMenor (A):
    menor = min(A)
    return menor
    

def MostraMaior(A):
    maior = max(A)
    return maior

menor = MostraMenor(A)    
maior = MostraMaior(A)
positivo = TotalPositivo(A)
negativo = TotalNegativo(A)

print ('O maior valor é: ', maior)
print ('O menor valor é: ', menor)
if positivo !=0:
    print ('A quantidade de positivos é: ', positivo)
elif positivo == 0:
    print ('nenhum número positivo foi digitado')
if negativo !=0:
    print ('A quantidade de negativos é: ', negativo)
elif negativo == 0:
    print ('nenhum número negativo foi digitado')