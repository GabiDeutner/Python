'''

11. Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se 
o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
− Triângulo Retângulo: possui um ângulo reto. (igual a 90º) 
− Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º) 
− Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)


'''
print('Digite o ângulo 1 em graus:')
A1 = int(input())
print('Digite o ângulo 2 em graus:')
A2 = int(input())
print('Digite o ângulo 3 em graus:')
A3 = int(input())
if(A1 == 90 or A2 == 90 or A3 == 90):
    print('Triângulo Retângulo')
elif(A1 > 90 or A2 > 90 or A3 > 90): 
    print('Triângulo Obtusângulo')
elif( A1 < 90 and A2 < 90 and A3 <90 ): 
    print('Triângulo Acutângulo')
else:
    print('não foi possível identificar')
