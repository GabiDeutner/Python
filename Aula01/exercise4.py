'''
4. Faça um programa para receber um valor e escrever se é “positivo”, “negativo” ou "elemento neutro".
'''
print('Digite um numero:')
numero = float(input())
if(numero>0):
    print('Valor é positivo')
elif(numero<0):
    print('Valor é negativo')
else:
    print('elemento neutro')
