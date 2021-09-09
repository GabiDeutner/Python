'''

5) Faça um programa que receba uma senha formada de quatro números inteiros, 
verifique se a senha está correta e, caso não esteja, solicite novamente a senha. 
Se a senha digitada for a correta, deverá ser apresentada a mensagem “Senha Correta”, 
caso contrário, “Senha Incorreta”.

'''
lista = []
senha = 0
n = 0
print("Digite uma senha com 4 caracteres:")
while n < 4:
     print("Digite o primeiro caracter:")
     s1= str(input())
     n = n + 1
     print("Digite o segundo caracter:")
     s2= str(input())
     n = n + 2
     print("Digite o terceiro caracter:")
     s3= str(input())
     n = n + 3
     print("Digite o quarto caracter:")
     s4= str(input())
     n = n + 4
senha = s1 + s2 + s3 + s4     
    
while lista != senha:
        print("Digite a senha:")
        lista = str(input())
        if senha != lista:
            print("Senha Incorreta!")
print("Senha Correta!")

