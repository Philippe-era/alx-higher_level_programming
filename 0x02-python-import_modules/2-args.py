#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    one = 1
    zero = 0

    count_num = len(sys.argv) - 1
    if count_num == zero:
        print("0 arguments.")
    elif count_num == one:
        print("1 argument:")
    else:
        print("{} arguments:".format(count_num))
    for initial in range(count_num):
        print("{}: {}".format(initial + 1, sys.argv[initial + 1]))

