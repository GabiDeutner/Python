
'''

1.Faça um programa que receba 1 número entre 1 e 999999999 e mostre esse valor por extenso. 
Fazer a verificação se o valor pertence ao intervalo solicitado.

'''

def imprime_num(c, d, u):
    if c=='9':
        cprint = print('novecentos ', end='')
    elif c=='8':
        cprint = print('oitocentos ', end='')
    elif c=='7':
        cprint = print('setecentos ', end='')
    elif c=='6':
        cprint = print('seiscentos ', end='')
    elif c=='5':
        cprint = print('quinhentos ', end='')
    elif c=='4':
        cprint = print('quatrocentos ', end='')
    elif c=='3':
        cprint = print('trezentos ', end='')
    elif c=='2':
        cprint = print('duzentos ', end='')
    elif c=='1':
        if d=='0' and u =='0':
            cprint = print('cem ')
        else:
            cprint = print('cento e ')
    elif c=='':
        cprint = print('')

    if d=='9':
        dprint = print ('noventa ', end='')
    elif d=='8':
        dprint = print('oitenta ', end='')
    elif d=='7':
        dprint = print('setenta ', end='')
    elif d=='6':
        dprint = print('sessenta ', end='')
    elif d=='5':
        dprint = print('cinquenta ', end='')
    elif d=='4':
        dprint = print('quarenta ', end='')
    elif d=='3':
        dprint = print('trinta ', end='')
    elif d=='2':
        dprint = print('vinte ', end='')
    elif d=='1':
        if u=='9':
            dprint = print ('dezenove ', end='')
        if u=='8':
            dprint = print ('dezoito ', end='')
        if u=='7':
            dprint = print ('dezessete ', end='')
        if u=='6':
            dprint = print ('dezesseis ', end='')
        if u=='5':
            dprint = print ('quinze ', end='')
        if u=='4':
            dprint = print ('quatorze ', end='')
        if u=='3':
            dprint = print ('treze ', end='')
        if u=='2':
            dprint = print ('doze ', end='')
        if u=='1':
            dprint = print ('onze ', end='')
        if u=='0':
            dprint = print ('dez ', end='')
    elif d == '':
        dprint = print('')

    if d != '1':
        if u=='9':
            uprint = print ('nove')
        elif u=='8':
            uprint = print ('oito')
        elif u=='7':
            uprint = print ('sete')
        elif u=='6':
            uprint = print ('seis')
        elif u=='5':
            uprint = print ('cinco')
        elif u=='4':
            uprint = print ('quatro')
        elif u=='3':
            uprint = print ('três')
        elif u=='2':
            uprint = print ('dois')
        elif u=='1':
            uprint = print ('um')
    elif u == '':
        uprint = print('')
    return print(cprint, dprint, uprint)
    
def imprime_unidade(u):
    if u=='9':
        uprint = print ('nove')
    elif u=='8':
        uprint = print ('oito')
    elif u=='7':
        uprint = print ('sete')
    elif u=='6':
        uprint = print ('seis')
    elif u=='5':
        uprint = print ('cinco')
    elif u=='4':
        uprint = print ('quatro')
    elif u=='3':
        uprint = print ('três')
    elif u=='2':
        uprint = print ('dois')
    elif u=='1':
        uprint = print ('um')
    return print(uprint)

def imprime_dezena(d,u):
    if d=='9':
        dprint = print ('noventa ', end='')
    elif d=='8':
        dprint = print('oitenta ', end='')
    elif d=='7':
        dprint = print('setenta ', end='')
    elif d=='6':
        dprint = print('sessenta ', end='')
    elif d=='5':
        dprint = print('cinquenta ', end='')
    elif d=='4':
        dprint = print('quarenta ', end='')
    elif d=='3':
        dprint = print('trinta ', end='')
    elif d=='2':
        dprint = print('vinte ', end='')
    elif d=='1':
        if u=='9':
            dprint = print ('dezenove ', end='')
        if u=='8':
            dprint = print ('dezoito ', end='')
        if u=='7':
            dprint = print ('dezessete ', end='')
        if u=='6':
            dprint = print ('dezesseis ', end='')
        if u=='5':
            dprint = print ('quinze ', end='')
        if u=='4':
            dprint = print ('quatorze ', end='')
        if u=='3':
            dprint = print ('treze ', end='')
        if u=='2':
            dprint = print ('doze ', end='')
        if u=='1':
            dprint = print ('onze ', end='')
        if u=='0':
            dprint = print ('dez ', end='')
    elif d == '':
        dprint = print('')

    if d != '1':
        if u=='9':
            uprint = print ('nove')
        elif u=='8':
            uprint = print ('oito')
        elif u=='7':
            uprint = print ('sete')
        elif u=='6':
            uprint = print ('seis')
        elif u=='5':
            uprint = print ('cinco')
        elif u=='4':
            uprint = print ('quatro')
        elif u=='3':
            uprint = print ('três')
        elif u=='2':
            uprint = print ('dois')
        elif u=='1':
            uprint = print ('um')
    return print(dprint, uprint)

s = str(input('digite um número: '))


if len(s) == 9:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
    c = s[len(s)-3:len(s)-2]
    um = s[len(s)-4:len(s)-3]
    dm = s[len(s)-5:len(s)-4]
    cm = s[len(s)-6:len(s)-5]
    uM= s[len(s)-7:len(s)-6]
    dM= s[len(s)-8:len(s)-7]
    cM= s[len(s)-9:len(s)-8]
elif len(s) == 8:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
    c = s[len(s)-3:len(s)-2]
    um = s[len(s)-4:len(s)-3]
    dm = s[len(s)-5:len(s)-4]
    cm = s[len(s)-6:len(s)-5]
    uM= s[len(s)-7:len(s)-6]
    dM= s[len(s)-8:len(s)-7]
    cM=''
elif len(s) == 7:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
    c = s[len(s)-3:len(s)-2]
    um = s[len(s)-4:len(s)-3]
    dm = s[len(s)-5:len(s)-4]
    cm = s[len(s)-6:len(s)-5]
    uM= s[len(s)-7:len(s)-6]
    dM=''
    cM=''
elif len(s) == 6:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
    c = s[len(s)-3:len(s)-2]
    um = s[len(s)-4:len(s)-3]
    dm = s[len(s)-5:len(s)-4]
    cm = s[len(s)-6:len(s)-5]
    uM=''
    dM=''
    cM=''
elif len(s) == 5:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
    c = s[len(s)-3:len(s)-2]
    um = s[len(s)-4:len(s)-3]
    dm = s[len(s)-5:len(s)-4]
elif len(s) == 4:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
    c = s[len(s)-3:len(s)-2]
    um = s[len(s)-4:len(s)-3]
    dm=''
    cm=''
    uM=''
    dM=''
    cM=''
elif len(s) == 3:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
    c = s[len(s)-3:len(s)-2]
elif len(s) == 2:
    u = s[len(s)-1:len(s)]
    d = s[len(s)-2:len(s)-1]
elif len(s) == 1:
    u = s[len(s)-1:len(s)]
elif len(s) == 0:
    print('o número é zero')
else:
    print('número fora do intervalo permitido')


if len(s) == 9:
    print(imprime_num(cM, dM, uM),'milhoes')
    print(imprime_num(cm, dm, um),'mil')
    print(imprime_num(c, d, u))
elif len(s) == 8:
    print(imprime_num(cM, dM, uM),'milhoes')
    print(imprime_num(cm, dm, um),'mil')
    print(imprime_num(c, d, u))
elif len(s) == 7:
    if uM == '1':
        print('Um milhão')
        print(imprime_num(cm, dm, um),'mil')
    else:
        print(imprime_num(cM, dM, uM),'milhoes')
        print(imprime_num(cm, dm, um),'mil')
        print(imprime_num(c, d, u))
elif len(s) == 6:
    print(imprime_num(cm, dm, um),'mil')
    print(imprime_num(c, d, u))
elif len(s) == 5:
    print(imprime_dezena(dm,um), 'mil')
    print(imprime_num(c, d, u))
elif len(s) == 4:
    print(imprime_num(cm, dm, um),'mil')
    print(imprime_num(c, d, u))
elif len(s) == 3:
    print(imprime_num(c, d, u))
elif len(s) == 2:
    print(imprime_dezena(d,u))
elif len(s) == 1:
    print(imprime_unidade(u))
else:
    print('número fora do intervalo permitido')