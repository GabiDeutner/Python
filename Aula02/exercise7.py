'''

7. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). 
Calcular e imprimir o seguinte: 
− Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área 
− Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área. 
− Se o número de lados for igual a 5 escrever PENTÁGONO.

'''
print('Digite o número de lados do polígono: ')
lados = float(input())
print('Digite a medida do lado (em centímetros):')
medida = float(input())

if(lados == 3):
    print('Digite a altura (em centímetros):')
    alt = float(input())
    area = medida*alt/2
    print('TRIÂNGULO, valor da área: ', area)
elif(lados == 4):
    area = medida*medida
    print('QUADRADO, valor da área: ', area)
elif(lados == 5):
    print('Digite a apótema (em centímetros):')
    ap = float(input())
    area = 5*medida*ap
    print('PENTÁGONO, valor da área: ', area)
else:
    print('Não foi possível calcular, tente novamente')