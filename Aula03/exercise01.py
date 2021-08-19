'''
1) Faça um programa em Python para escrever os números pares entre 0 e 500.
'''
for num in range (0,501,1):
    if num % 2 == 0:
        print("O número", num, "é par")
    else:
        print("O número", num, "é impar")
