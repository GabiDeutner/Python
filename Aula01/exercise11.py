'''
11. A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais
 de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%.
  Escreva um programa que leia o número de horas trabalhadas em um mês, o salário por hora e
   escreva o salário total do funcionário, que deverá ser acrescido das horas extras, 
   caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
 '''
 
 print('Digite o numero de horas trabalhadas no mês:')
HoraMes = float(input())
print('Digite o quanto você ganha por hora:')
valor = float(input())
HoraSemana=(HoraMes/4)
if(HoraSemana<=40):
    salario = HoraMes*valor
    print('o salário total é R$', salario, 'reais')
else:
    HoraExtra = (HoraMes-160)
    SalarioExtra = HoraExtra * (1.5*valor)
    SalarioBase = (160*valor)
    salario= SalarioExtra + SalarioBase
    print('o salário total é R$', salario, 'reais')
