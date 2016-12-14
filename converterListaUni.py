listaUni = []

def unirLista(lista):
    for item in lista:
        listaUni.append(item)


while 1 :
    print '\nNova lista \n'
    lista1 = []
    while 1:
        args = raw_input('Itens da lista: ')
        if args == '':
            break
        else:
            lista1.append(args)
    if lista1 == []:
        break
    else:
        unirLista(lista1)
print listaUni
