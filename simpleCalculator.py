#!/usr/bin/env python3


def basic():
    print('Basic calculator is activated')


def scientific():
    print('Scientific calculator is activated')


print('Select calculator type:\n1.Basic\n2.Scietific\n')

calculatorType = int(input('Enter calculator number: '))
2
if calculatorType == 1:
    basic()
elif calculatorType == 2:
    scientific()
else:
    print('Enter valid number of calculator type, please!')
