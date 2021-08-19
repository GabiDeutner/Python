'''
2) Faça um programa em Python que conte de 1 a 100 e a 
cada múltiplo de 10 emita uma mensagem: “Múltiplo de 10”.

'''
for num in range (1,101,1):
    if (num % 10 == 0):
        print("O número", num, "é múltiplo de 10")

