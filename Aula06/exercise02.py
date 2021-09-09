'''
2. Faça um programa que leia a idade, altura e peso de 10 pessoas e mostre:
a. o número de pessoas com idade maior que 50;
b. a média das alturas das pessoas com menos de 70 e mais de 50 anos;
c. a porcentagem de pessoas com menos de 50 quilos.

'''


idade50 = []
alt5070 = []
peso50 = []

for N in range (1,11,1):
    print('pessoa número', N)
    print('Digite sua idade:')
    idade = int(input())
    print('Digite sua altura em centimetros:')
    alt = int(input())
    print('Digite seu peso em quilos:')
    peso = int(input())
    if idade > 50:
        idade50.append(idade)
    if idade > 50 and idade < 70:
        alt5070.append(alt)
    if peso < 50:
        peso50.append(peso)
    N = N+1

if  len(idade50) != 0:
    print ('o número de pessoas com idade maior que 50 é:', len(idade50))
elif len(idade50) == 0:
    print ('não há pessoas com idade maior que 50')

if len(alt5070) != 0:
    media = sum(alt5070)/len(alt5070)
    print ('a média das alturas das pessoas com menos de 70 e mais de 50 anos é:', media)
elif len(alt5070) == 0:
    print ('não há pessoas com menos de 70 e mais de 50 anos')
    
if len(peso50) != 0:
    porcent = len(peso50)/10 * 100
    print ('a porcentagem de pessoas com menos de 50 quilos é:', porcent, '%')
elif len(peso50) == 0:
    print ('não há pessoas com menos de 50 quilos')
        
        