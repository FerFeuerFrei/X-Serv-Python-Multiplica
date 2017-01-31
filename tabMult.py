# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:03:56 2017

@author: ftorrijo
"""

rango = range(1,11)
for num in rango:
    print "\nTabla del " + str(num) + '\n' + '############'
    for num2 in rango:
        print str(num) + ' x ' + str(num2) + ' = ' + str(num*num2)