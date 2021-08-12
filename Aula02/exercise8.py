'''

8. Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso. 
− Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO. 
− Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

'''
print('Digite o número de lados do polígono: ')
lados = float(input())

if(lados == 3):
    print('Digite a medida do lado (em centímetros):')
    medida = float(input())
    print('Digite a altura (em centímetros):')
    alt = float(input())
    area = medida*alt/2
    print('TRIÂNGULO, valor da área: ', area)
elif(lados == 4):
    print('Digite a medida do lado (em centímetros):')
    medida = float(input())
    area = medida*medida
    print('QUADRADO, valor da área: ', area)
elif(lados == 5):
    print('Digite a medida do lado (em centímetros):')
    medida = float(input())
    print('Digite a apótema (em centímetros):')
    ap = float(input())
    area = 5*medida*ap
    print('PENTÁGONO, valor da área: ', area)
elif(lados<3):
    print('NÃO É UM POLÍGONO')
elif(lados>5):
    print('POLÍGONO NÃO IDENTIFICADO')
else:
    print('Não foi possível calcular, tente novamente')