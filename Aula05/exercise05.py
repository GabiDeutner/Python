'''

 5) Foi feita uma pesquisa entre os habitantes de uma região. 
 Foram coletados os dados de idade, sexo (1/2 – masculino/feminino) e salário. 
 Faça um programa que calcule e mostre:
a) A média dos salários do grupo;
b) A maior e a menor idade do grupo;
c) A quantidade de mulheres na região;
d) A idade e o sexo da pessoa que possui o menor salário;
Finalize a entrada de dados ao ser digitada uma idade negativa.


'''

i = 0
s = 0
sa = 0
contsa = 0
totsa = 0
m = 0
f = 0
menorsa = 99999999999999
menorid = 99999999999999
maiorid = 0
idademenorsa = 0
sexomenorsa = 0

while i >= 0:
    print("Digite sua idade:")
    i = int(input())
    
    if i >= 0:
        if maiorid < i:
            maiorid = i
        if menorid > i:
            menorid = i
    else:
        print("Não existe idade negativa")
    
    print("Digite seu sexo:")
    print("1 - masculino")
    print("2 - feminino:")
    s = int(input())
    if s == 1:
        m = m + 1 
    if s == 2:
        f = f + 1 
    print("Digite seu salário:")
    sa = float(input())
    totsa = totsa + sa
    contsa = contsa + 1
    
    if menorsa > sa:
        menorsa = sa
        idademenorsa = i
        sexomenorsa = s

med1 = totsa/contsa


print("A média dos salários do grupo é:", med1)
print("A maior idade é:", maiorid, "anos")
print("A menor idade é:", menorid, "anos")
print("A quantidade de mulheres na região é:", f, "mulheres")
print("A idade da pessoa com menor salário é:", idademenorsa, "anos")

if sexomenorsa == 1:
    print("O sexo da pessoa com menor salário é masculino" )
elif sexomenorsa == 2:
    print("O sexo da pessoa com menor salário é feminino" )