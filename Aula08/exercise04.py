'''
 4ª Questão:
 Refaça o exercício 1, usando funções, 
 Crie, para isso, as funções CalcularMedia e VerificaAcimaMedia.
'''

A= []
c=0
soma = 0
m = 0 
n=0
med = 0
total=0
num=0

for c in range (0,100,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    c = c + 1
    
soma = sum(A)

def CalcularMedia (A):
    med = soma / len(A)
    return med

def VerificaAcimaMedia (A):
    total = list(A)
    m = 0
    for n in total:
        if n > med:
            m = m + 1 
    return m 

med = CalcularMedia (A)
m = VerificaAcimaMedia (A)

print ('A média é: ', med)
print ('Quantidade de números acima da média: ', m)
print ('A soma dos elementos do vetor é: ', soma)