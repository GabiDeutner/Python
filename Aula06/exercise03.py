'''
3. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:

a. a média do salário da população;
b. a média do número de filhos;
c. o maior salário;
d. a porcentagem de pessoas com salário até R$ 1500,00.

Faça um programa que receba os dados de 10 habitantes e exiba um relatório com os valores pedidos.


'''

lista1500 = []
listasal = []
listafil = []


for N in range (1,11,1):
    print('pessoa número', N)
    print('Digite o seu salário em reais:')
    sal = float(input())
    listasal.append(sal)
    print('Digite o número de filhos:')
    fil = int(input())
    listafil.append(fil)
    if sal <= 1500:
        lista1500.append(sal)
    N = N+1

if sum(listasal) != 0:
    media = sum(listasal)/10
    print ('a média do salário da população é:', media)
elif sum(listasal) == 0:
    print ('não há pessoas com salário nessa pesquisa')
    
if sum(listafil) != 0:
    media2 = sum(listafil)/10
    print ('a média do número de filhos da população é:', media2)
elif sum(listafil) == 0:
    print ('não há pessoas com filhos nessa pesquisa')
    
if sum(listasal) != 0:
    print ('o maior salário é:', max(listasal))
elif sum(listasal) == 0:
    print ('não há pessoas com salário nessa pesquisa')

if sum(lista1500) != 0:
    porcent = len(lista1500)/10 * 100
    print ('a porcentagem de pessoas com salário de até R$ 1500,00 é:', porcent, '%')
elif sum(lista1500) == 0:
    print ('não há pessoas com salário de até R$ 1500,00 nessa pesquisa')
        
        