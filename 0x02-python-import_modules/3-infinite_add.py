#!/usr/bin/python3

if __name__ == "__main__":
    
    import sys

    altogether = 0
    for initial in range(len(sys.argv) - 1):
        altogether += int(sys.argv[initial + 1])
    print("{}".format(altogether))

