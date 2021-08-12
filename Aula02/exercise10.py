'''

10. Escreva um programa que leia as medidas dos lados de um triângulo e escreva 
se ele é Equilátero, Isósceles ou Escaleno. Sendo que: 
− Triângulo Equilátero: possui os 3 lados iguais. 
− Triângulo Isóscele: possui 2 lados iguais. 
− Triângulo Escaleno: possui 3 lados diferentes.

'''
print('Digite o lado 1:')
L1 = int(input())
print('Digite o lado 2:')
L2 = int(input())
print('Digite o lado 3:')
L3 = int(input())
if(L1 == L2 == L3):
    print('Triângulo Equilátero')
elif(L1 == L2 or L1 == L3 or L2 == L3): 
    print('Triângulo Isósceles')
elif(L1 != L2 or L1 != L3 or L2 != L3): 
    print('Triângulo Escaleno')
else:
    print('não foi possível identificar')
