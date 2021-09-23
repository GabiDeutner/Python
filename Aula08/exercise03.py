'''
3ª Questão: 
Criar um vetor chamado nota1, outro vetor chamado nota2 
e um terceiro vetor chamado nota3, que armazenarão as notas de 3 provas de uma turma de alunos.
Faça um programa em Python que:
(a) Permita ao usuário entrar com as notas 1, 2 e 3 de 100 alunos.
(b) Encontre o aluno com maior média geral.
(c) Para cada aluno diga se ele foi aprovado, 
reprovado ou se está de exame. 
Considere o valor 7 para aprovação. 
O aluno só poderá fazer exame se tiver nota maior ou igual a 3 e menor que 7. 
Será considerado reprovado o aluno que tiver nota inferior a 3.

'''

nota1=[]
nota2=[]
nota3=[]
lista=[]
maiormed=0 
n1=0 
n2=0 
n3=0
media=0 
c=0

for c in range (0,100,1):
    print('Digite a nota 1:')
    n1 = int(input())
    nota1.append(n1)
    print('Digite a nota 2:')
    n2 = int(input())
    nota2.append(n2)
    print('Digite a nota 3:')
    n3 = int(input())
    nota3.append(n3)
    media = ((n1+n2+n3)/3)
    lista.append(media)
    if media >= 7:
        print ('Aluno aprovado')
    elif media < 7 and media >=3:
        print ('Aluno de exame')
    elif media < 3:
        print ('Aluno reprovado')
    c = c+1

maiormed = max(lista)

print ('A maior média geral é: ', maiormed)