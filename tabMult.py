#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Tabla de multiplicar

"""

# Rango de 1 a 10
rango = range(1,11)
 
# Ahora imprimimos desde la tabla de multiplicar del 1 hasta la
# tabla de multiplicar del 10

for num in rango:
    print "\nTabla del " + str(num) + '\n' + ''
    for num2 in rango:
        print str(num) + 'x' + str(num2) + '=' + str(num*num2)
