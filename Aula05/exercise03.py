'''

3) Faça um programa que simule uma urna eletrônica. 
A tela a ser apresentada deverá ser da seguinte forma:
As opções são:
1. Candidato Mauro Ubando
2. Candidato Kay Xadois
3. Candidato Fikaru Riko
4. Nulo
5. Branco
6. Terminar
Entre com o seu voto:
O programa deverá ler os votos dos eleitores e, quando for digitado o número 6, 
apresentar as seguintes informações:
a) O número de votos de cada candidato;
b) A porcentagem de votos nulos;
c) A porcentagem de votos brancos;
d) O candidato vencedor.



'''
x = 0
y = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
contagem = 0
vencedor = 0

while y != 6 :
    print("As opções de candidatos são:")
    print("1. Candidato Mauro Ubando")
    print("2. Candidato Kay Xadois")
    print("3. Candidato Fikaru Riko")
    print("4. Nulo")
    print("5. Branco")
    print("6. Terminar")
    print("Entre com o seu voto:")
    y = int(input())
    contagem = contagem + 1
    
    if y == 1:
        print("Você votou em:")
        print("1. Candidato Mauro Ubando")
        c1 = c1 + 1
    elif y == 2:
        print("Você votou em:")
        print("2. Candidato Kay Xadois")
        c2 = c2 + 1
    elif y == 3:
        print("Você votou em:")
        print("3. Candidato Fikaru Riko")
        c3 = c3 + 1
    elif y == 4:
        print("Você votou em:")
        print("4. Nulo")
        c4 = c4 + 1
    elif y == 5:
        print("Você votou em:")
        print("5. Branco")
        c5 = c5 + 1
    print ("------------------------------------------------------------")
    print ("------------------------------------------------------------")

p4 = (c4/contagem)*100
p5 = (c5/contagem)*100

print("Número de votos no Candidato Mauro Ubando:", c1, "votos")
print("Número de votos no Candidato Kay Xadois:", c2, "votos")
print("Número de votos no Candidato Fikaru Riko:", c3, "votos")
print("A porcentagem de votos nulos:", p4, "%")
print("A porcentagem de votos em branco:", p5, "%")

if c1 > c2 and c1 > c3:
    print("O Candidato vencedor é: Mauro Ubando")
elif c2 > c1 and c2 > c3:
    print("O Candidato vencedor é: Kay Xadois")
elif c3 > c1 and c3 > c2:
    print("O Candidato vencedor é: Fikaru Riko") 