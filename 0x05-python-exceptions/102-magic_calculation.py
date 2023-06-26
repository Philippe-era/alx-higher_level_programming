#!/usr/bin/python3

def magic_calculation(a, b):
    final = 0
    one = 1
    three = 3
    for initial in range(one, three):
        try:
            if initial > a:
                raise Exception('Too far')
            else:
                final += a ** b / initial
        except:
            final = b + a
            break
    return (final)


