import reader

def dec_to_bin(dec_str):
    dec_str = int(dec_str[1:])
    binary = bin(dec_str)[2:]
    
    binary = binary.zfill(7)
    return binary

import struct
import re
import math
import struct

#ASSUMPTION ONLY NORMAL NUMBERS ARE GIVEN AS INPUT

def calculate_exponent_and_mantissa(decimal_num):
    bias = 3
    value = abs(decimal_num)
    exponent_value = int(math.log2(value))

    if exponent_value < -bias:
        return '0' * 8

    if exponent_value > (2 ** (3 - 1)) - 1:
        return '0' * 5 + '1' + '0' * 2

    exponent_binary = bin(exponent_value + bias)[2:].zfill(3)
    mantissa = (value / (2 ** exponent_value) - 1) * (2 ** 5)
    mantissa_binary = bin(int(mantissa))[2:].zfill(5)

    return exponent_binary + mantissa_binary


def decimal_to_ieee(decimal_str):
    decimal_num = float(decimal_str[1:])
    return calculate_exponent_and_mantissa(decimal_num)

def gen_address(count):
    address = bin(count)[2:]
    address = address.zfill(7)
    return address


