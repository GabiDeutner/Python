'''
Classe Aluno: Crie uma classe Aluno, 
que deve ter os seguintes atributos: nome, curso, tempoSemDormir (em horas). 
Essa classe deverá ter os seguintes métodos: 
– estudar (que recebe como parâmetro a quantidade de horas de estudo e acrescenta tempoSemDormir ) 
– Dormir (que recebe como parâmetro a quantidade de horas de sono e reduz tempoSemDormir ) 
Crie um código de teste da classe, criando um objeto da classe aluno 
e usando os métodos estudar e dormir. Ao final imprima quanto tempo o aluno está sem dormir.
'''

class Aluno():

    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def setNome(self, nome):
        self.nome = nome
    
    def setCurso(self, curso):
        self.curso = curso
        
    def setTempoSemDormir(self, tempoSemDormir):
        self.tempoSemDormir = tempoSemDormir
    
    def getEstudar(self):
        self.estudo = float(input("Digite a quantidade de horas de estudo:"))
        self.tempoSemDormir = self.estudo
        return self.tempoSemDormir
    
    def getDormir(self):
        self.sono = float(input("Digite a quantidade de horas de sono:"))
        self.tempoSemDormir = self.sono - self.tempoSemDormir
        return self.tempoSemDormir

N=str(input("Digite o nome do aluno:"))
C=str(input("Digite o curso:"))
T=int(0)
  
aluno = Aluno(N,C,T)
print("=====================================")
print("O nome do aluno é:", N)
print("O curso do aluno é:", C)
aluno.getEstudar()
print("O tempo sem dormir é: ", aluno.getDormir(), "horas")