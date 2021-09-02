'''

4) Faça um programa que mostre a tabuada de um número N (N será lido do teclado). 

'''

c = 0
r = 0

print("Digite o número da tabuada:")
x = int(input())
while c != 11:
    r = x * c
    print(x,'X',c,'=',r)
    c = c + 1