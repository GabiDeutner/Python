'''

1.Faça uma função que receba a altura inicial de uma árvore, a taxa de crescimento 
ao ano e uma quantidade n de anos. Esta função deve calcular altura desta árvore após n anos.

'''
class Arvore():
    
    def __init__(self, alt, cresc, anos):
        self.alt = alt
        self.cresc = cresc
        self.anos = anos
        
    def setAltura(self, alt):
        self.alt = alt
    
    def setCrescimento(self, cresc):
        self.cresc = cresc
        
    def setAnos(self, anos):
        self.anos = anos
        
    def getCalculo(self):
        return self.alt + (self.cresc * self.anos)
    
Alt = float(input("Digite a altura inicial da árvore em metros: "))
Cresc = float(input("Digite a taxa de crescimento em metros ao ano: "))
A = int(input("Digite a quantidade de anos para prever o crescimento da árvore: "))
arvore = Arvore(Alt,Cresc,A)
print("A altura da árvore vai ser de ",arvore.getCalculo(),"metros")
