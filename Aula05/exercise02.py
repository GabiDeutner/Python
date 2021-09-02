'''

2) Faça um programa que receba uma senha formada de quatro números inteiros, 
verifique se a senha está correta e, caso não esteja, solicite novamente a senha. 
Se a senha digitada for a correta, deverá ser apresentada a mensagem “Senha Correta”, 
caso contrário, “Senha Incorreta”.

'''
x = 0
y = 0

print("Cadastre uma senha de quatro caracteres:")
while y < 4 :
    print("Digite o primeiro caractere:")
    s1 = str(input())
    y = y + 1
    print("Digite o segundo caractere:")
    s2 = str(input())
    y = y + 2
    print("Digite o terceiro caractere:")
    s3 = str(input())
    y = y + 3
    print("Digite o quarto caractere:")
    s4 = str(input())
    y = y + 4
senha = s1+s2+s3+s4

while x != senha:
    print("Digite a senha:")
    x = str(input())
print("senha correta!")