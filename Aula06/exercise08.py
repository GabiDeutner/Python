'''

 8) Foi feita uma pesquisa entre os habitantes de uma região. 
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
listasa=[]
listamasc=[]
listafem=[]
listai=[]
menorsa = 99999999999999
idademenorsa = 0
sexomenorsa = 0
menori = 99999999999999999


print("Digite sua idade:")
i = int(input())
listai.append(i)

while i >= 0:
    
    
    print("Digite seu sexo:")
    print("1 - masculino")
    print("2 - feminino:")
    s = int(input())
    if s == 1:
        listamasc.append(s) 
    if s == 2:
        listafem.append(s)
        
    print("Digite seu salário:")
    sa = float(input())
    listasa.append(sa)

    
    if menorsa > sa:
        menorsa = sa
        idademenorsa = i
        sexomenorsa = s
    
    if i < menori:
        menori = i
        
    print('-------------------------------------------------------')

    print("Digite sua idade:")
    i = int(input())
    listai.append(i)

med1 = sum(listasa)/len(listasa)


print("A média dos salários do grupo é:", med1)
print("A maior idade é:", max(listai), "anos")
print("A menor idade é:", menori, "anos")
print("A quantidade de mulheres na região é:", len(listafem), "mulheres")
print("A idade da pessoa com menor salário é:", idademenorsa, "anos")

if sexomenorsa == 1:
    print("O sexo da pessoa com menor salário é masculino" )
elif sexomenorsa == 2:
    print("O sexo da pessoa com menor salário é feminino" )