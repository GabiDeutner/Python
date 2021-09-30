'''

 4ª Questão: Refaça o exercício 1, usando funções, 
 Crie, para isso, as funções CalcularMediaAcim, CalcularMediaAbaixo, e VerificaAcimaMedia.
 
 Faça um programa em Python que leia um vetor A de 6 números. 
 Depois disso, calcular a média e quantos números estão acima da média e 
 quantos estão abaixo da média. Calcule, também, a soma dos elementos acima da média do vetor.

'''

A= []
c=0
soma = 0
acima = 0
acimasoma=0
ac = []
ac2=[]
ab=[]
n=0
med = 0
total=0
num=0

for c in range (0,6,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    c = c + 1
    
soma = sum(A)
med = soma / len(A)


def CalcularMediaAcim (A):
    total = list(A)
    acima = 0
    for n in total:
        if n > med:
            ac.append(n)
    acima = len(ac)
    return acima 
    
def CalcularMediaAbaixo (A):
    total = list(A)
    abaixo = 0
    for n in total:
        if n < med:
            ab.append(n)
    abaixo = len(ab)
    return abaixo 
    
def VerificaAcimaMedia (A):
    total = list(A)
    acimasoma = 0
    for n in total:
        if n > med:
            ac2.append(n)
    acimasoma = sum(ac2)
    return acimasoma

acima = CalcularMediaAcim (A)
abaixo = CalcularMediaAbaixo (A)
acimasoma = VerificaAcimaMedia (A)

print ('A média é: ', med)
print ('Quantidade de números acima da média: ', acima)
print ('Quantidade de números abaixo da média: ', abaixo)
print ('A soma dos elementos acima da média do vetor é: ', acimasoma)