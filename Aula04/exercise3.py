'''
3. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, 
coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:

a. a média do salário da população;
b. a média do número de filhos;
c. o maior salário;
d. a porcentagem de pessoas com salário até R$ 1500,00.

Faça um programa que receba os dados de 10 habitantes e exiba um relatório com os valores pedidos.


'''

somasal = 0
somafil = 0
somasal2 = 0
maiorsal = 0


for N in range (1,11,1):
    print('pessoa número', N)
    print('Digite o seu salário em reais:')
    sal = float(input())
    somasal = somasal + sal
    print('Digite o número de filhos:')
    fil = int(input())
    somafil = somafil + fil
    if sal <= 1500:
        somasal2 = somasal2 + 1
    if sal > maiorsal:
        maiorsal = sal
    N = N+1

if somasal != 0:
    media = somasal/10
    print ('a média do salário da população é:', media)
elif somasal == 0:
    print ('não há pessoas com salário nessa pesquisa')
    
if somafil != 0:
    media2 = somafil/10
    print ('a média do número de filhos da população é:', media2)
elif somafil == 0:
    print ('não há pessoas com filhos nessa pesquisa')
    
if maiorsal != 0:
    print ('o maior salário é:', maiorsal)
elif maiorsal == 0:
    print ('não há pessoas com salário nessa pesquisa')

if somasal2 != 0:
    porcent = somasal2/10 * 100
    print ('a porcentagem de pessoas com salário de até R$ 1500,00 é:', porcent, '%')
elif somasal2 == 0:
    print ('não há pessoas com salário nessa pesquisa')
        
        