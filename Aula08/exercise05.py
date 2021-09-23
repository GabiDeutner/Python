'''
 5ª Questão:
 Refaça o exercício 2, usando funções. 
 Crie, para isso, as funções MostraMaior, MostraMenor, TotalPar e TotalImpar.
'''

A= []
c=0
par = 0
impar = 0
soma = 0
total1=0 
total2=0
menor = 99999999999999999
maior=0

for c in range (0,3,1):
    print('Digite um numero:')
    num = int(input())
    A.append(num)
    
def TotalPar(A):
    total1 = list(A)
    np = 0
    par=0
    for np in total1:
        if np % 2 ==0:
            par = par + 1
    return par
        
def TotalImpar(A):
    total2 = list(A)
    ni = 0
    impar=0
    for ni in total2:
        if ni % 2 !=0:
            impar = impar + 1
    return impar

def MostraMenor (A):
    menor = min(A)
    return menor
    

def MostraMaior(A):
    maior = max(A)
    return maior

menor = MostraMenor(A)    
maior = MostraMaior(A)
par = TotalPar(A)
impar = TotalImpar(A)

print ('O maior valor é: ', maior)
print ('O menor valor é: ', menor)
print ('A quantidade de pares é: ', par)
print ('A quantidade de ímpares é: ', impar)