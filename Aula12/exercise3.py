'''

3.    Faça  uma  função  que  receba  um  valor  inicial  aplicado,  a  taxa  de  juros  ao  ano. 
Esta  função  deve  calcular  a quantidade de anos necessários para duplicar o saldo inicial

'''
class Calculos():
    
    def __init__(self,valor,ano, taxa):
        self.valor = valor
        self.ano= ano
        self.taxa = taxa

    def setValor(self, valor):
        self.valor = valor

    def setAno(self, ano):
        self.ano = ano
        
    def setTaxa(self, taxa):
        self.taxa = taxa
    
    def getCalculo(self, valor, ano, taxa):
        vdobro = self.valor * 2
        while self.valor <= vdobro:
            self.valor = self.valor * (1+ self.taxa/100)
            self.ano = self.ano + 1
        return self.ano

v = float(input("Digite o valor inicial: "))
a = 0
t = float(input("Digite a taxa de juros ao ano em %: "))
calculos = Calculos(v,a,t)
print('Foi necessários ', calculos.getCalculo(v,a,t),'anos para duplicar o valor inicial')
