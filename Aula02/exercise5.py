'''

5. Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) 
e escrevê-los em ordem crescente.

'''
print('Digite um valor inteiro:')
v1 = int(input())
print('Digite um valor inteiro:')
v2 = int(input())
print('Digite um valor inteiro:')
v3 = int(input())

print('Agora vou mostrar os valores em ordem crescente:')

if(v1<v2<v3):
    print(v1, v2, v3)
elif(v1<v3<v2):
    print(v1, v3, v2)
elif(v2<v1<v3):
    print(v2, v1, v3)
elif(v2<v3<v1):
    print(v2, v3, v1)
elif(v3<v1<v2):
    print(v3, v1, v2)
else:
    print(v3, v2, v1)