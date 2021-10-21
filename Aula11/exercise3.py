'''
3.Classe Livro: Crie uma classe Livro que possui os atributos nome, 
qtdPaginas, autor e preço. 
Crie os métodos getPreco para obter o valor do preco 
e o método setPreco para setar um novo valor do preco.
'''

class Livro():

    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco

    def setNome(self, nome):
        self.nome = nome
    
    def setQtdPaginas(self, qtdPaginas):
        self.qtdPaginas = qtdPaginas
        
    def setAutor(self, autor):
        self.autor = autor
    
    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        self.preco = float(input("Digite o preço novo do livro:"))
        return self.preco
    
N=str(input("Digite o nome do livro:"))
Q=float(input("Digite a quantidade de páginas:"))
A=str(input("Digite o autor:"))
P=float(input("Digite o preço antigo:"))


    
livro = Livro(N,Q,A,P)
print("=====================================")
print("O nome do livro é:", N)
print("A quantidade de páginas é:", Q)
print("O autor é: ", A)
print("O preço antigo é: ", P)
print("O preço novo é: ", livro.getPreco())