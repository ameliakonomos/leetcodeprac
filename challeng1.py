#challenge 1:
#Given two binary strings,
# return their sum (also a binary string).
import numpy as np

def binary_func(a,b):
    a = str(a)
    b = str(b)
    max_len = int(len(a) + len(b))

    #adds zeros at the beginning of the string until it reaches max
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    #our result
    result = ''
    #carry
    carry = 0

    #edit string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        carry = 0 if r < 2 else 1

    if carry != 0: result = '1' + result

    return result.zfill(max_len)


print(binary_func(11900, 1))