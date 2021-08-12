'''

6. Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) 
de uma pessoa, construa um programa que calcule e imprima seu peso ideal, 
utilizando as seguintes Fórmulas: 
para homens: (72.7 * Altura) – 58 
para mulheres: (62.1 * Altura) – 44.7

'''
print('Digite um número para o seu sexo: ')
print('1 : Feminino: ')
print('2 : Masculino ')
sexo = int(input())
print('Digite a sua altura em metros:')
alt = float(input())

print('Agora vou mostrar o seu peso ideal:')

if(sexo == 1):
    peso = (62.1 * alt) - 44.7
    print('Seu peso ideal é: ', peso)
elif(sexo == 2):
    peso = (72.7 * alt) - 58
    print('Seu peso ideal é: ', peso)
else:
    print('Não foi possível calcular, tente novamente')