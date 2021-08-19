'''
4) Faça um programa em Python para ler 10 números inteiros e 
escrever a soma e a média dos números lidos.

'''

soma = 0

for num in range (1,11,1):
    print('Digite um numero:')
    num = int(input())
    soma = soma + num

media = soma/10

print ("a soma dos números é:", soma)
print ("a média dos números é:", media)