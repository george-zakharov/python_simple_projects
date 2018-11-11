#!/usr/bin/env python3

import sys
import math


def calculator_handler(calculator_type):
    result = ''

    if calculator_type == 1:
        print('Basic calculator is activated')
        source_data = {
            'first_number': float(input('Type in first number: ')),
            'operation': str(input('Type in operation sign: ')).strip(),
            'second_number': float(input('Type in second number: ')),
        }

        if source_data['operation'] not in ['+', '-', '*', '/']:
            sys.exit('Operation sign must be one of: + - * /')

        result = do_calculations(source_data, calculator_type)
    elif calculator_type == 2:
        print('Scientific calculator is activated')
        source_data = {
            'operation': str(input('Type in operation: ')),
            'number': float(input('Type in number: ')),
        }

        if source_data['operation'] not in ['ceil', 'exp', 'log10', 'log2', 'sqrt', 'cos', 'sin', 'pi', 'e']:
            sys.exit('Operation sign must be one of: ceil, exp, log10, log2, sqrt, cos, sin, pi, e')

        result = do_calculations(source_data, calculator_type)

    print('Result is:')
    print(result)


def do_calculations(data, calculator_type):
    result = 0

    if calculator_type == 1:
        if data['operation'] is '+':
            result = data['first_number'] + data['second_number']
        elif data['operation'] is '-':
            result = data['first_number'] - data['second_number']
        elif data['operation'] is '*':
            result = data['first_number'] * data['second_number']
        elif data['operation'] is '/':
            result = data['first_number'] / data['second_number']
    elif calculator_type == 2:
        if data['operation'] == 'ceil':
            result = math.ceil(data['number'])
        elif data['operation'] == 'exp':
            result = math.exp(data['number'])
        elif data['operation'] == 'log10':
            result = math.log10(data['number'])
        elif data['operation'] == 'log2':
            result = math.log2(data['number'])
        elif data['operation'] == 'sqrt':
            result = math.sqrt(data['number'])
        elif data['operation'] == 'cos':
            result = math.cos(data['number'])
        elif data['operation'] == 'sin':
            result = math.sin(data['number'])
        elif data['operation'] == 'pi':
            result = math.pi
        elif data['operation'] == 'e':
            result = math.e

    return result


print('Select calculator type:\n1.Basic\n2.Scietific\n')
calculator_type = int(input('Enter calculator number: '))
if calculator_type in [1, 2]:
    calculator_handler(calculator_type)
else:
    sys.exit('Enter valid number of calculator type, please!')
