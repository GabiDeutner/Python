'''

2.Faça um programa para calcular e mostrar  o  valor  a  pagar  pela  anuidade  de  
uma  associação  em  cada um dos  meses.  O valor  básico,  informado  pelo  usuário, 
é  válido  apenas  para  o  mês  de  janeiro.  Nos  meses subsequentes, há um acréscimo 
de 5% ao mês de juros (com juros sobre juros). *Por exemplo, valor em janeiro: R$100; 
em fevereiro, custa R$105; em março, custa R$110,25; e, em dezembro, R$171,03.

'''
class Calculos():
    
    def __init__(self,valor):
        self.valor = valor

    def setValor(self, valor):
        self.valor = valor
    
    def setValor(self, cont):
        self.cont = cont
    
    def getCalcular(self):
            self.valor = self.valor * 1.05
            return self.valor

v = float(input("Digite o valor inicial: "))

calculos = Calculos(v)
m=1
while m<=12:
    print('No mês', m, 'a anuidade é de valor:', calculos.getCalcular())
    m= m+1
