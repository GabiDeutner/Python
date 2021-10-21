class Pessoa:  # A criação de uma classe começa pelo uso da palavra reservada class,
               # seguida do nome da classe e dois pontos;
    nome = None
    idade = None
    def __init__(self, nome, idade): # Aqui temos a definição do construtor da classe,
                                     # que é um método especial chamado __init__.
                                     # Como todo método em Python, sua declaração começa com def e,
                                     # entre parênteses, estão os parâmetros, incluindo o parâmetro
                                     # obrigatório self, que está presente em todos os métodos;
        self.nome = nome # O corpo do método deve estar indentado, como manda a sintaxe da linguagem.
                         # Aqui estamos apenas atribuindo os valores recebidos por parâmetro aos
                         # atributos da classe;
        self.idade = idade

    # Criação dos métodos set de todos os atributos da classe Pessoa que serão responsáveis por
    # modificar os atributos desta classe.   
      
    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getAnoNascimento(self, anoAtual):
        return anoAtual - pessoa.idade
    
pessoa = Pessoa("Jackie", 54) 
print (pessoa.getAnoNascimento(2021))
print(pessoa.nome)
print (pessoa.idade)

pessoa.setNome("Joao")

print(pessoa.nome)
print (pessoa.idade)

p=input()
i=int(input())

pessoa = Pessoa(p,i)

print(pessoa.nome)
print(pessoa.idade)