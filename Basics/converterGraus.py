#-*- coding: utf-8 -*-

def celsius_to_fahrenheit(n):
    return (9/5.0)*n + 32

def fahrenheit_to_celsius(n):
    return (n-32)/1.8

num = float(raw_input("Digite a temperatura: "))
escala = raw_input("Digite a unidade em que está: ")

if escala == 'F':
    print 'Valor em celsius: ',fahrenheit_to_celsius(num)
elif escala == 'C':
    print 'Valor em fahrenheit: ',celsius_to_fahrenheit(num)
