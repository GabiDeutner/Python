'''
1.Classe Triangulo: Crie uma classe que modele um triangulo:                 
– Atributos:       LadoA,  LadoB,  LadoC
– Métodos:        calcular Perímetro, getMaiorLado;                         
Crie um programa que utilize esta classe. 
Ele deve pedir ao usuário que informe as medidas de um triangulo. 
Depois, deve criar um objeto com as medidas e imprimir seu perímetro e maior lado.     
'''

class Triangulo():

    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC
    
    def setLadoA(self, LadoA):
        self.LadoA = LadoA
    
    def setLadoB(self, LadoB):
        self.LadoB = LadoB
        
    def setLadoC(self, LadoC):
        self.LadoC = LadoC
    
    def getCalcularPerimetro(self):
        return self.LadoA + self.LadoB + self.LadoC
        
    def getMaiorLado(self):
        if self.LadoA > self.LadoB and self.LadoA > self.LadoC:
            return self.LadoA
        elif self.LadoB > self.LadoA and self.LadoB > self.LadoC:
            return self.LadoB
        elif self.LadoC > self.LadoA and self.LadoC > self.LadoB:
            return self.LadoC
    
A=int(input("Digite o valor do lado A:"))
B=int(input("Digite o valor do lado B:"))
C=int(input("Digite o valor do lado C:"))
    
triangulo = Triangulo(A,B,C)
print("O perímetro do triângulo é: ", triangulo.getCalcularPerimetro())
print("O maior lado é de:",triangulo.getMaiorLado())