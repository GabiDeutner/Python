'''

1.Faça um programa que receba 1 número entre 1 e 999999999 e mostre esse valor por extenso. 
Fazer a verificação se o valor pertence ao intervalo solicitado.

'''

def imprime_num(c,d,u):
    if c==9:
        cprint = print('novecentos', end='')
    elif c==8:
        cprint = print('oitocentos', end='')
    elif c==7:
        cprint = print('setecentos', end='')
    elif c==6:
        cprint = print('seiscentos', end='')
    elif c==5:
        cprint = print('quinhentos', end='')
    elif c==4:
        cprint = print('quatrocentos', end='')
    elif c==3:
        cprint = print('trezentos', end='')
    elif c==2:
        cprint = print('duzentos', end='')
    elif c==1:
        if d==0 and u ==0:
            cprint = print('cem')
        else:
            cprint = print('cento e:')

    if d==9:
        dprint = print ('noventa ')
    elif d==8:
        dprint = print('oitenta')
    elif d==7:
        dprint = print('setenta')
    elif d==6:
        dprint = print('sessenta')
    elif d==5:
        dprint = print('cinquenta')
    elif d==4:
        dprint = print('quarenta')
    elif d==3:
        dprint = print('trinta')
    elif d==2:
        dprint = print('vinte')
    elif d==1:
        if u==9:
            dprint = print ('dezenove ')
        if u==8:
            dprint = print ('dezoito ')
        if u==7:
            dprint = print ('dezessete ')
        if u==6:
            dprint = print ('dezesseis ')
        if u==5:
            dprint = print ('quinze ')
        if u==4:
            dprint = print ('quatorze ')
        if u==3:
            dprint = print ('treze ')
        if u==2:
            dprint = print ('doze ')
        if u==1:
            dprint = print ('onze ')
        if u==0:
            dprint = print ('dez ')

    if d != 1:
        if u==9:
            uprint = print ('nove')
        elif u==8:
            uprint = print ('oito')
        elif u==7:
            uprint = print ('sete')
        elif u==6:
            uprint = print ('seis')
        elif u==5:
            uprint = print ('cinco')
        elif u==4:
            uprint = print ('quatro')
        elif u==3:
            uprint = print ('três')
        elif u==2:
            uprint = print ('dois')
        elif u==1:
            uprint = print ('um')
        return cprint, dprint, uprint

cM = int(input('digite centena de milhão: '))
dM = int(input('digite dezena de milhão '))
uM = int(input('digite unidade de milhão: '))

cm = int(input('digite centena de milhar: '))
dm = int(input('digite dezena de milhar: '))
um = int(input('digite unidade de milhar: '))

c = int(input('digite centena: '))
d = int(input('digite dezena: '))
u = int(input('digite unidade: '))


if cM == 1:
    print('Um milhão')
elif cM == 0:
    print('')
else:
    print(imprime_num(cM,dM,uM),'milhoes')

if cm != 0:
    print(imprime_num(cm,dm,um))
elif cM == 0:
    print('')

if c != 0:
    print(imprime_num(c,d,u))
elif c == 0:
    print('')