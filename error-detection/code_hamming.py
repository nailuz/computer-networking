# -*- coding: utf-8 -*-
import math
from itertools import chain

def parity_bits_quantity(wordsize):
    return int(math.log(wordsize, 2))+1

def parity_indexes(index, wordsize):
    for i in range(index, wordsize+1, index*2):
        yield range(i, i+index)

def check_parity(index, word):
    array = chain(*parity_indexes(index, len(word)))
    test = compare(list(array), word)
    if not test[0]:
        return test[2]
    else:
        return 0 

def compare(bits, word):
    count = 0
    for i in bits:
        if word[i-1] == '1' and i !=  bits[0]:
            count += 1
    if count%2: return [word[bits[0]-1] == '1', 'IMPAR', bits[0]]
    else: return [word[bits[0]-1] == '0', 'PAR', bits[0]]

def check(data):
    print('Seu valor: ', data)
    size = len(data)
    print('Size:', str(size))
    qt_parity_bits = parity_bits_quantity(size)
    print('Parity bits quantity:', qt_parity_bits)
    count = 0
    for row in range(qt_parity_bits):
        index = 2 ** row
        count += check_parity(index, data)
    print('Seu erro esta na posição ', str(count))

check('0111111')
