'''

1.Faça um programa que receba 1 número entre 1 e 999999999 e mostre esse valor por extenso. 
Fazer a verificação se o valor pertence ao intervalo solicitado.

'''

def imprime_c(c,d):
    if c=='9':
        cprint = print('novecentos ')
    elif c=='8':
        cprint = print('oitocentos ')
    elif c=='7':
        cprint = print('setecentos ')
    elif c=='6':
        cprint = print('seiscentos ')
    elif c=='5':
        cprint = print('quinhentos ' )
    elif c=='4':
        cprint = print('quatrocentos ' )
    elif c=='3':
        cprint = print('trezentos ')
    elif c=='2':
        cprint = print('duzentos ')
    elif c=='1':
        if d=='0' and u =='0':
            cprint = print('cem ')
        else:
            cprint = print('cento e:')
            
    return cprint

def imprime_d(d,u):
    if d=='9':
        dprint = print ('noventa ')
    elif d=='8':
        dprint = print('oitenta ')
    elif d=='7':
        dprint = print('setenta ')
    elif d=='6':
        dprint = print('sessenta ')
    elif d=='5':
        dprint = print('cinquenta ')
    elif d=='4':
        dprint = print('quarenta ')
    elif d=='3':
        dprint = print('trinta ')
    elif d=='2':
        dprint = print('vinte ')
    elif d=='1':
        if u=='9':
            dprint = print ('dezenove ')
        if u=='8':
            dprint = print ('dezoito ')
        if u=='7':
            dprint = print ('dezessete ')
        if u=='6':
            dprint = print ('dezesseis ')
        if u=='5':
            dprint = print ('quinze ')
        if u=='4':
            dprint = print ('quatorze ')
        if u=='3':
            dprint = print ('treze ')
        if u=='2':
            dprint = print ('doze ')
        if u=='1':
            dprint = print ('onze ')
        if u=='0':
            dprint = print ('dez ')
    return dprint

def imprime_u(u):
    if d != '1':
        if u=='9':
            uprint = print (' nove ')
        elif u=='8':
            uprint = print (' oito ')
        elif u=='7':
            uprint = print (' sete')
        elif u=='6':
            uprint = print (' seis')
        elif u=='5':
            uprint = print (' cinco')
        elif u=='4':
            uprint = print (' quatro')
        elif u=='3':
            uprint = print (' três')
        elif u=='2':
            uprint = print (' dois')
        elif u=='1':
            uprint = print (' um')
    else:
        uprint = print('')
    return uprint

n = str(input('Digite o número: '))
print (len(n))


u = len(n)

if u == 9:
    u = n[8]
    d = n[7]
    c = n[6]
    um = n[5]
    dm = n[4]
    cm = n[3]
    uM = n[2]
    dM = n[1]
    cM = n[0]
    print(imprime_c(cM,dM))
    print(imprime_d(dM,uM))
    print(imprime_u(uM),'milhoes')
    print(imprime_c(cm,dm))
    print(imprime_d(dm,um))
    print(imprime_u(um), 'mil')
    print(imprime_c(c,d))
    print(imprime_d(d,u))
    print(imprime_u(u))
elif u == 8:
    u = n[7]
    d = n[6]
    c = n[5]
    um = n[4]
    dm = n[3]
    cm = n[2]
    uM = n[1]
    dM = n[0]
    print(imprime_d(dM,uM))
    print(imprime_u(uM),'milhoes')
    print(imprime_c(cm,dm))
    print(imprime_d(dm,um))
    print(imprime_u(um), 'mil')
    print(imprime_c(c,d))
    print(imprime_d(d,u))
    print(imprime_u(u))
elif u == 7:
    u = n[6]
    d = n[5]
    c = n[4]
    um = n[3]
    dm = n[2]
    cm = n[1]
    uM = n[0]
    print(imprime_u(uM),'milhoes')
    print(imprime_c(cm,dm))
    print(imprime_d(dm,um))
    print(imprime_u(um), 'mil')
    print(imprime_c(c,d))
    print(imprime_d(d,u))
    print(imprime_u(u))
elif u == 6:
    u = n[5]
    d = n[4]
    c = n[3]
    um = n[2]
    dm = n[1]
    cm = n[0]
    print(imprime_c(cm,dm))
    print(imprime_d(dm,um))
    print(imprime_u(um), 'mil')
    print(imprime_c(c,d))
    print(imprime_d(d,u))
    print(imprime_u(u))    
elif u == 5:    
    u = n[4]
    d = n[3]
    c = n[2]
    um = n[1]
    dm = n[0]
    print(imprime_d(dm,um))
    print('mil')
    print (imprime_c(c,d),imprime_d(d,u),imprime_u(u))
    '''
    print(imprime_c(c,d))
    print(imprime_d(d,u))
    print(imprime_u(u))
    '''
elif u == 4:
    u = n[3]
    d = n[2]
    c = n[1]
    um = n[0]
    print(imprime_u(um))
    print('mil')
    print(imprime_c(c,d))
    print(imprime_d(d,u))
    print(imprime_u(u))
elif u == 3:    
    u = n[2]
    d = n[1]
    c = n[0]
    print(imprime_c(c,d))
    print(imprime_d(d,u))
    print(imprime_u(u))
elif u == 2:
    u = n[1]
    d = n[0]
    print(imprime_d(d,u))
    print(imprime_u(u))
else:
    u == n[0]
    print(imprime_u(u))