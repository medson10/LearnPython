#-*- coding: utf-8 -*-

def opsDicionario(dici):
    soma = 0
    total = 0
    for valor in dici.values():
        soma = soma + valor
        total = total + 1
    media = soma / total
    print 'Soma = ',soma
    print "Media = ",media
    print 'Variação = ',(soma/media)

codigos = []
valores = []
while True:
    arg = raw_input('Digite um codigo: ')
    if arg == '':
        break
    else:
        codigos.append(int(arg))

while True:
    arg2 = raw_input('Digite um valor: ')
    if arg2 == '':
        break
    else:
        valores.append(int(arg2))

dic = {'Codigo':codigos,'Valores':valores}
opsDicionario(dic)
