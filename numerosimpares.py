varA = int(raw_input('Digite o primeiro valor: '))
varB = int(raw_input('Digite o segundo valor: '))
cont = 0
for x in range(varA+1,varB):
    if x % 2 != 0:
        print x
        cont = cont + 1
print ''
print 'Total de numeros impares: ',cont
