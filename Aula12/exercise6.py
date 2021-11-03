'''
6. Uma  empresa  de  turismo realiza  excursões  familiares  para  subir
a  Pedra  da  Gávea.  
No  entanto,  é  necessário que as seguintes regras sejam obedecidas:
· grupo de no mínimo 5 pessoas
· pelo menos a metade dos participantes devem ser maior de idade
· não pode haver integrantes com menos de 11 anos
· o integrante mais velho será escolhido o líder da excursão.
Faça um programa que leia o nome e a idade das pessoas de uma excursão familiar
e diga se esse grupo satisfaz as regras e pode participar da excursão
(informando, também, o nome do seu líder) ou se este grupo não satisfaz as
regras e, por isso, não pode participar da excursão.
Obs: o término da entrada dos participantes da excursão ocorre quando for
 digitado um nome == 'x’
'''

class Turismo():
   
    def __init__(self,idade,nome,vetor3, menor):
        self.idade = idade
        self.nome = nome
        self.vetor3 = vetor3
        self.menor = menor
   
    def setTotal(self, total):
        self.total = total
           
    def setIdade(self, idade):
        self.idade = idade
       
    def setNome(self, nome):
        self.nome = nome
   
    def setVetor3(self, vetor3):
        self.vetor3 = vetor3
   
    def setMenor(self, menor):
        self.menor = menor
   
    def getVetor(self):
        idade = []
        nome = []
        vetor3 = []
        menor = []
        idade2 = int(0)
        nome2 = str('')
        while nome2 != 'x':
            print ('Digite o seu nome:')
            nome2 = str(input())
            if nome2 != 'x':
                nome.append(nome2)
            else:
                break
           
            print ('Digite a sua idade:')
            idade2 = int(input())
            idade.append(idade2)
            if idade2 > 18:
                vetor3.append(idade2)
            if idade2 < 11:
                menor.append(idade2)
       
        var1 = str('')
        var2 = str('')
        var3 = str('')
        var4 = str('')
        total2 = len(vetor3)
        if len(nome) >= 5:
            if total2 < len(nome)/2:
                var2 = str(print('O grupo não pode participar, pois mais da metade é menor de idade!'))
            elif total2 >= len(nome)/2:
                if menor != []:
                    var3 = str(print('O grupo não pode participar, pois existem pessoas menores de 11 anos!'))
                else:
                    var4 = str(print('O grupo pode participar!'))
        else:
                var1 = str(print('O grupo é menor que 5 pessoas!'))            
               
        var5 = str('')
        posicao = int(0)
        lider = str('')
        posicao = idade.index(max(idade))
        lider = nome[posicao]
        var5 = str(print('O líder do grupo é: ', lider))

        return idade, vetor3, menor, nome, var1, var2, var3, var4, var5
   

idade = []
nome = []
vetor3 = []
menor = []
grupo = Turismo(idade,nome,vetor3, menor)

resposta = grupo.getVetor()
