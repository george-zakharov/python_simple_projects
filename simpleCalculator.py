#!/usr/bin/env python3

import sys, math


def basic():
    print('Basic calculator is activated')
    source_data = {
        'first_number': float(input('Type in first number: ')),
        'operation': str(input('Type in operation sign: ')),
        'second_number': float(input('Type in second number: ')),
    }

    if source_data['operation'] not in ['+', '-', '*', '/']:
        print('Operation sign must be one of: + - * /')

    result = do_basic_calculations(source_data)

    print('Result is:')
    print(result)


def do_basic_calculations(data):
    result = 0
    if data['operation'] is '+':
        result = data['first_number'] + data['second_number']
    elif data['operation'] is '-':
        result = data['first_number'] - data['second_number']
    elif data['operation'] is '*':
        result = data['first_number'] * data['second_number']
    elif data['operation'] is '/':
        result = data['first_number'] / data['second_number']

    return result


def scientific():
    print('Scientific calculator is activated')


print('Select calculator type:\n1.Basic\n2.Scietific\n')
calculator_type = int(input('Enter calculator number: '))
if calculator_type == 1:
    basic()
elif calculator_type == 2:
    scientific()
else:
    sys.exit('You should enter valid number of calculator type, please!')
