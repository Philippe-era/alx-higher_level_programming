#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# function that gives positive numbers only
num_check = abs(number) % 10
number_check = 0
second_number = 5
if number < number_check:
    num_check = -num_check
print("Last digit of {} is {} and is ".format(number, num_check), end="")
if num_check > second_number:
    print("greater than 5")
elif num_check == number_check:
    print(f"{number_check}")
else:
    print("less than 6 and not 0")

