'''

3ª Questão: (1,00 ponto). Criar um vetor chamado nota1, outro vetor chamado nota2 e 
um terceiro vetor chamado trabalho, que armazenarão as notas de 2 provas e 1 trabalho 
de uma turma de alunos.
Faça um programa em Python que:
(a) Permita ao usuário entrar com as nota1, nota2 e trabalho de 8 alunos.
(b) Calcule e armazene a média de cada aluno,  
usando a fórmula (nota1* 0,3 + nota2 * 0,4 + trabalho*0,3) 
Encontre o aluno com maior média.
(c) Para cada aluno diga se ele foi aprovado, reprovado ou se está de exame. 
Considere o valor 7 para aprovação. 
O aluno só poderá fazer exame se tiver média maior ou igual a 3 e menor que 7, 
desde que nenhuma das notas seja 0. 
Será considerado reprovado o aluno que tiver nota inferior a 3.

'''

nota1=[]
nota2=[]
trabalho=[]
med=[]
maiormed=0 
n1=0 
n2=0 
t1=0
media=0 
c=0
cc=0
x=0


for c in range (0,8,1):
    print('Digite a nota 1:')
    n1 = int(input())
    nota1.append(n1)
    print('Digite a nota 2:')
    n2 = int(input())
    nota2.append(n2)
    print('Digite a nota de trabalho:')
    t1 = int(input())
    trabalho.append(t1)
    media = (n1* 0.3 + n2 * 0.4 + t1*0.3)
    med.append(media)
    if media >= 7:
        print ('media: ',media,' Aluno aprovado')
    elif media < 3:
        print ('media: ',media,' Aluno reprovado')
    elif n1==0 :
        print ('media: ',media,' Aluno reprovado')
    elif n2==0 :
        print ('media: ',media,' Aluno reprovado')
    elif t1==0 :
        print ('media: ',media,' Aluno reprovado') 
    elif media < 7 and media >=3 and n1!=0 and n2!=0 and t1!=0:
        print ('media: ',media,' Aluno de exame')

    c = c+1

maiormed = max(med)

print('--------------------------------------------------------')

for x in med:
    cc = cc+1
    if(x == maiormed):
        print('A maior média geral é',maiormed,'do aluno', cc)