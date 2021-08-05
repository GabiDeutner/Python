'''
8. Faça um programa que receba quatro notas de um aluno, calcule e apresente a média aritmética das notas e a mensagem “aprovado” ou “reprovado”, considerando, para aprovação, média 8,0.
'''
print('Digite a nota 1 do aluno:')
nota1 = float(input())
print('Digite a nota 2 do aluno:')
nota2 = float(input())
print('Digite a nota 3 do aluno:')
nota3 = float(input())
print('Digite a nota 4 do aluno:')
nota4 = float(input())
media=(nota1+nota2+nota3+nota4)/4
if(media>=8):
    print('aprovado')
else:
    print('reprovado')
