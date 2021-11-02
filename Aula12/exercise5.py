'''
5. Escreva um programa que pergunte a idade de 6 pessoas, calcule e mostre:
a) a quantidade de pessoas menores de idade (idade < 18 anos)
b) média de idade destas pessoas
c) a idade da pessoa mais velha
d) percentual de pessoas com mais de 20 anos
'''

class Idades():
   
    def __init__(self,vetor1,vetor2,vetor3):
        self.vetor1 = vetor1
        self.vetor2 = vetor2
        self.vetor3 = vetor3
               
    def setVetor1(self, vetor1):
        self.vetor1 = vetor1
       
    def setVetor2(self, vetor2):
        self.vetor2 = vetor2
   
    def setVetor3(self, vetor3):
        self.vetor3 = vetor3
   
    def getCalculo(self):
        self.vetor1 = []
        self.vetor2 = []
        self.vetor3 = []
        for n in range(0,6,1):            
            print ('Digite a sua idade:')
            idade = int(input())
            vetor1.append(idade)
            if idade < 18:
                vetor2.append(idade)
            elif idade > 20:
                vetor3.append(idade)
               
        media = sum(vetor1)/6
        maximo = max(vetor1)
        permaiorId = (len(vetor3) * 100) / len(vetor1)
       
        var1 = str(print('Quantidade de pessoas menores de idade: ', len(vetor2)))
        var2 = str(print('A média de idade é: ', media))
        var3 = str(print('A idade da pessoa mais velha é: ', maximo))
        var4 = str(print('Percentual de pessoas com mais de 20 anos: ', permaiorId))
       
        return var1, var2, var3, var4

vetor1 = []
vetor2 = []
vetor3 = []
idades = Idades(vetor1,vetor2,vetor3)

resposta = idades.getCalculo()