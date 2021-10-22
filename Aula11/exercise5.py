'''
5. Classe carro: Crie uma classe chamada Carro com as seguintes propriedades:
 •Um veículo tem um determinado consumo de combustível (medidos em km / litro) 
 e uma certa quantidade de combustível no tanque.
•O consumo é especificado no construtor e o nível de combustível inicial é 0.
•Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa 
distância, reduzindo o nível de combustível no tanque de gasolina. Esse método 
recebe como parâmetro a distância em km.
•Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
•Forneça um método adicionarGasolina( ), para abastecer o tanque.
•Faça um programa para testar a classe Carro.

Exemplo de uso: meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
 meuFusca.andar(100); # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.
'''

class Carro():

    def __init__(self, distancia, gasolina, andar):
        self.distancia = distancia
        self.gasolina = gasolina
        self.andar = andar

    def setDistancia(self, distancia):
        self.distancia = distancia
    
    def setObterGasolina(self, gasolina):
        self.gasolina = gasolina
    
    def getAdicionarGasolina(self):
        adicionar = float(input("Quantos litros de gasolina para abastecer o tanque do veículo: "))
        self.gasolina = self.gasolina + adicionar
        return self.gasolina
        
    def setAndar(self):
        self.andar = self.distancia * self.gasolina
    
    def getGasolinaRestante(self):
        percorrida = float(input("Qual foi a distância percorrida: "))
        gasolinaRestante = ( percorrida - self.andar ) / self.distancia
        return gasolinaRestante

D=int(input("Quantidade de quilômetros que o veículo anda por litro de combustível: "))
O=float(0)
A=float(0)
carro = Carro(D,O,A)
carro.getAdicionarGasolina()
print("A gasolina restante é de: ", carro.getGasolinaRestante(), "litros")