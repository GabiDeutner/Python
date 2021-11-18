'''

x = slice(0,3,1)
começa do 0, anda 3 pra frente, de um em um

n = str(input('Digite o número: '))
print (len(n))

'''
s = '123456789'
#    01234
print(s[len(s)-1:len(s)]) #pega sempre o último número 9
print(s[len(s)-2:len(s)-1]) #pega sempre o penúltimo número 8
print(s[len(s)-3:len(s)-2]) #pega sempre o penúltimo número 7
print(s[len(s)-4:len(s)-3]) #pega sempre o penúltimo número 6
print(s[len(s)-5:len(s)-4]) #pega sempre o penúltimo número 5
print(s[len(s)-6:len(s)-5]) #pega sempre o penúltimo número 6
print(s[len(s)-7:len(s)-6]) #pega sempre o penúltimo número 7
print(s[len(s)-8:len(s)-7]) #pega sempre o penúltimo número 8
print(s[len(s)-9:len(s)-8]) #pega sempre o penúltimo número 9

x = slice(0,1,1)
print(s[x])