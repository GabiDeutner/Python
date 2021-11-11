'''
2.Faça um programa que receba 1 número entre 1 e 3999 e mostre esse valor em algarismos romanos.
Importante: As letras são sempre maiúsculas e o Zero não é representado.

'''
unidades = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII','IX', 'X']
dezenas = ['' , '', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
centenas = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
milhares = ['', 'M', 'MM', 'MMM']
                    
numero = int(input('Digite o número: '))
print(f'O numero {numero} em numeral romano pode ser escrito como: ')


if numero >= 1000 and numero < 3999:
    print(milhares[int(str(numero)[0])], end='')
    numero = numero - int(str(numero)[0])*1000
if numero >= 100 and numero < 1000:
    print(centenas[int(str(numero)[0])], end='')
    numero = numero - int(str(numero)[0])*100
if numero !=0:
    print(end='' )
if numero < 20:
    print(unidades[numero])
    numero = 0
elif numero >= 20:
    print(dezenas[int(str(numero)[0])], end='')
    numero = numero - int(str(numero)[0])*10
if numero != 0:
    print(unidades[numero])