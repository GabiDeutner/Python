'''
2. Classe Funcionário: Crie a classe Funcionário. 
Um funcionário tem um nome e um salário. 
Escreva um construtor com dois parâmetros (nome e salário) 
e o método aumentarSalario (porcentualDeAumento) 
que aumente o salário do funcionário em uma certa porcentagem.   
'''

class Funcionario():

    def __init__(self, nome, salario, porcent):
        self.nome = nome
        self.salario = salario
        self.porcent = porcent

    def setNome(self, nome):
        self.nome = nome
    
    def setSalario(self, salario):
        self.salario = salario
        
    def setPorcentagem(self, porcent):
        self.porcent = porcent
    
    def getAumentarSalario(self):
        return (self.salario * self.porcent/100) + self.salario
    
N=str(input("Digite o nome:"))
S=float(input("Digite o salário:"))
P=float(input("Digite a porcentagem de aumento em %:"))

    
funcionario = Funcionario(N,S,P)
print("O salário do funcionário é:", S)
print("O percentual de aumento de salário foi:", P, "%")
print("O salário com o aumento é de: ",funcionario.getAumentarSalario())