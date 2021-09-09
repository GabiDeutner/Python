'''

7) Faça um programa que mostre a tabuada de um número N (N será lido do teclado). 

'''

c = 0
r = 0
lista=[]

print("Digite o número da tabuada:")
N = int(input())
while c != 11:
    r = N * c
    lista.append(r)
    print(N,'X',c,'=',r)
    c = c + 1
print('Os produtos da tabuada do número', N, 'foram:',lista)