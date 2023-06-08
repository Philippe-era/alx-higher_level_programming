#!/usr/bin/python3

if __name__ == "__main__":
    
    from calculator_1 import add, sub, mul, div 
    import sys
    three = 3
    one = 1
    if len(sys.argv) - 1 != three:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(one)

    calculation = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(calculation.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(one)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))

