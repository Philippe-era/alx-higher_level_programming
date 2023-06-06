
#!/usr/bin/python3

first = 1
last = 101
fizz = 3
buzz = 5
zero = 0
def fizzbuzz():
    for num_check in range(first, last):
        if num_check % fizz == zero and num_check % buzz == zero:
            print("FizzBuzz ", end="")
        elif num_check % fizz == zero:
            print("Fizz ", end="")
        elif num_check % buzz == zero:
            print("Buzz ", end="")
        else:
            print("{} ".format(num_check), end="")

