
n = 99999999
operacao = ''
num1 = 0
num2 = 0

def calsoma(num1,num2):
    print('Digite o primeiro número:')
    num1 = int(input())
    print('Digite o segundo número:')
    num2 = int(input())
    soma = num1 + num2
    return soma

def calsubtracao(num1,num2):
    print('Digite o primeiro número:')
    num1 = int(input())
    print('Digite o segundo número:')
    num2 = int(input())
    sub = num1 - num2
    return sub
    
def calmultiplicacao(num1,num2):
    print('Digite o primeiro número:')
    num1 = int(input())
    print('Digite o segundo número:')
    num2 = int(input())
    mult = num1 * num2
    return mult
    
def caldivisao(num1,num2):
    print('Digite o número que será dividido:')
    num1 = int(input())
    print('Digite o número divisor:')
    num2 = int(input())
    if num2 != 0:
        div = num1 / num2
    else:
        div = 'não existe divisão por zero'
    return div

while n != 0:
    print('Digite a operação que desejada:')
    print(' + para adição ')
    print(' - para subtração ')
    print(' * para multiplicação ') 
    print(' / para divisão')
    print(' X para sair')
    operacao = str(input())

    if (operacao == '+'):
        soma = calsoma(num1, num2)
        print('A soma foi de: ', soma)
    elif(operacao == '-'):
        sub = calsubtracao(num1, num2)
        print('A subtração foi de: ', sub)
    elif(operacao == '*'):
        mult = calmultiplicacao(num1, num2)
        print('A multiplicação foi de: ', mult)
    elif(operacao == '/'):
        div = caldivisao(num1, num2)
        print('O resultado da divisão foi: ', div)
    elif(operacao == 'x'):
        n = 0
    else:
        print('Operação inválida')