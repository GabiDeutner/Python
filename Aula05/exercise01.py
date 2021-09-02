'''

1) Faça um programa que leia número inteiros  maiores que zero. 
Quando for digitado o número zero, o programa deverá apresentar quantos números foram digitados  
e a média dos mesmos.

'''
s = 0
c = 0
x = 99999999

while x != 0:
    print("Digite um número:")
    x = int(input())
    if x != 0 :
        s = x + s
        c = c + 1
med = s / c 
print("quantidade de números digitados: ", c)
print("média dos números digitados: ", med)