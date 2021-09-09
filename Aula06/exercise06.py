'''

6) Faça um programa que simule uma urna eletrônica. 
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
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
listavoto=[]
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
    listavoto.append(y)
    
    if y == 1:
        c1.append(y)
    elif y == 2:
        c2.append(y)
    elif y == 3:
        c3.append(y)
    elif y == 4:
        c4.append(y)
    elif y == 5:
        c5.append(y)
    print ("------------------------------------------------------------")
    print ("------------------------------------------------------------")

p4 = (len(c4)/len(listavoto))*100
p5 = (len(c5)/len(listavoto))*100

print("Número de votos no Candidato Mauro Ubando:", len(c1), "votos")
print("Número de votos no Candidato Kay Xadois:", len(c2), "votos")
print("Número de votos no Candidato Fikaru Riko:", len(c3), "votos")
print("A porcentagem de votos nulos:", p4, "%")
print("A porcentagem de votos em branco:", p5, "%")

if len(c1) > len(c2) and len(c1) > len(c3):
    print("O Candidato vencedor é: Mauro Ubando")
elif len(c2) > len(c1) and len(c2) > len(c3):
    print("O Candidato vencedor é: Kay Xadois")
elif len(c3) > len(c1) and len(c3) > len(c2):
    print("O Candidato vencedor é: Fikaru Riko") 