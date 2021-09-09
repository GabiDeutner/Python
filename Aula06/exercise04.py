'''

4) Faça um programa que leia número inteiros  maiores que zero. 
Quando for digitado o número zero, o programa deverá apresentar quantos números foram digitados  
e a média dos mesmos.

'''
x = 99999999
lista=[]

while x != 0:
    print("Digite um número:")
    x = int(input())
    if x != 0 :
        lista.append(x)
med = sum(lista) / len(lista)
print("quantidade de números digitados: ", len(lista))
print("média dos números digitados: ", med)