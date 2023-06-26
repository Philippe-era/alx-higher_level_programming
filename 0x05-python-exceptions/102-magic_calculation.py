#!/usr/bin/python3

def magic_calculation(a, b):
    final = 0
    three = 3
    one = 1
    for initial in range(one, three):
        try:
            if initial > a:
                raise Exception('Too far')
            else:
                result += a ** b / initial
        except:
            result = b + a
            break
    return (result)


