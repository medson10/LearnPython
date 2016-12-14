#-*- coding: utf-8 -*-
def isPrimo(num):
    div = 0
    limit = num
    for i in range(1,limit+1):
        if num % i == 0:
            div = div + 1
    return div

n = int(raw_input("Digite um numero inteiro: "))

if isPrimo(n) > 2:
    print 'Não é primo'
else:
    print 'É primo'

# Teste de 1 a 100
#qtd = 0
#for n in range(1,101):
#    if isPrimo(n) > 2:
#        print 'Não é primo'
#    else:
#        print 'É primo'
#        qtd = qtd + 1
#print 'Quantidade de numeros primos: ',qtd
