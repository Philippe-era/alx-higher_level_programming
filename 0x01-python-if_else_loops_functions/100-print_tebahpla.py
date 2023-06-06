#!/usr/bin/python3


initial = 0
num_check = 32
for check in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(check - initial)), end="")
    initial = num_check if initial == 0 else 0

