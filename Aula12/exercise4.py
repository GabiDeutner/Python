'''
4.    Faça  uma  função  que  receba  a  altura  inicial  de  dois  meninos  
(Huguinho  e  Luisinho).  Esta  função  deve perguntar quantos cm cada um
cresceu ao ano, até que Huguinho esteja mais alto que Luisinho ou que ambos
tenham  parado  de  crescer (quantidade  de  cm  lida  == 0). Essa  função
deve  retornar  quantos  anos  levou  para que Huguinho tenha ficado mais
alto que Luisinho ou caso contrário.
'''

class Alturas():
   
    def __init__(self,hug,h2,luis,l2,ano,nome):
        self.hug = hug
        self.h2 = h2
        self.luis = luis
        self.l2 = l2
        self.ano = ano
        self.nome = nome

    def setHuguinho(self, hug):
        self.hug = hug

    def setHuguinho2(self, h2):
        self.h2 = h2
   
    def setLuisinho(self, luis):
        self.luis = luis

    def setLuisinho2(self, l2):
        self.l2 = l2
   
    def setAno(self, ano):
        self.ano = ano
   
    def setNome(self, nome):
        self.nome = nome
   
    def getCalculaAltura(self,hug,h2,luis,l2,ano,nome):
        while self.hug <= self.luis:
            self.h2 = int(input('Digite quantos centimetros Huguinho cresceu no ano: '))
            self.l2 = int(input('Digite quantos centimetros Luisinho cresceu no ano: '))
            self.hug = self.hug + self.h2
            self.luis = self.luis + self.l2
            self.ano = self.ano + 1
           
            if self.h2 == 0 and self.l2 == 0:
                break

        if self.luis < self.hug:
           self.nome = str('Huguinho ser o mais alto')
        elif self.hug < self.luis:
             self.nome = str('Luisinho ser o mais alto')
        elif self.hug == self.luis:
             self.nome = str('Huguinho tem a mesma altura de Luisinho')
        var1=str(print('Foram necessários',self.ano,'anos para ', self.nome))
        return var1

hug = int(input('Digite a altura inicial de Huguinho em centímetros: '))
h2 = int(0)
luis = int(input('Digite a altura inicial de Luisinho em centímetros: '))
l2 = int(0)
ano = 0
nome = str('')
alturas = Alturas(hug,h2,luis,l2,ano,nome)

print(alturas.getCalculaAltura(hug,h2,luis,l2,ano,nome))