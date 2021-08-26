'''
1. Faça um programa que receba 10 números e mostre a soma dos números ímpares e a soma dos números pares.


'''
somapar = 0 
somaimpar = 0 

for num in range (0,10,1):
    print('Digite um numero:')
    num = int(input())
    if num % 2 == 0:
        somapar = somapar + num
    elif num % 2 != 0:
        somaimpar = somaimpar + num

if somaimpar == 0:        
    print('Não foram digitados números ímpares')
    print('soma dos pares:',somapar)
elif somapar == 0:        
    print('Não foram digitados números pares')
    print('soma dos ímpares:',somaimpar)
elif somapar and somaimpar != 0:
    print('soma dos ímpares:',somaimpar)
    print('soma dos pares:',somapar)

