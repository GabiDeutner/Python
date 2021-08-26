'''
2. Faça um programa que leia a idade, altura e peso de 10 pessoas e mostre:
a. o número de pessoas com idade maior que 50;
b. a média das alturas das pessoas com menos de 70 e mais de 50 anos;
c. a porcentagem de pessoas com menos de 50 quilos.

'''

somaidade = 0
somaalt = 0
somapeso = 0
somaalt2 = 0

for N in range (1,11,1):
    print('pessoa número', N)
    print('Digite sua idade:')
    idade = int(input())
    print('Digite sua altura em centimetros:')
    alt = int(input())
    print('Digite seu peso em quilos:')
    peso = int(input())
    if idade > 50:
        somaidade = somaidade + 1
    if idade > 50 and idade < 70:
        somaalt = somaalt + alt
        somaalt2 = somaalt2 + 1
    if peso < 50:
        somapeso = somapeso + 1
    N = N+1

if  somaidade != 0:
    print ('o número de pessoas com idade maior que 50 é:', somaidade)
elif somaidade == 0:
    print ('não há pessoas com idade maior que 50')

if somaalt != 0:
    media = somaalt/somaalt2
    print ('a média das alturas das pessoas com menos de 70 e mais de 50 anos é:', media)
elif somaalt == 0:
    print ('não há pessoas com menos de 70 e mais de 50 anos')
    
if somapeso != 0:
    porcent = somapeso/10 * 100
    print ('a porcentagem de pessoas com menos de 50 quilos é:', porcent, '%')
elif somapeso == 0:
    print ('não há pessoas com menos de 50 quilos')
        
        