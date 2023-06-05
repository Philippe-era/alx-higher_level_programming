#!/usr/bin/python3
first_num = 39
second_num = 67
third_num = 107
fourth_num = 112
last_num = 6
phrase = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
phrase = phrase[first_num:second_num] + phrase[third_num:fourth_num] + phrase[0:last_num]
print(phrase)

