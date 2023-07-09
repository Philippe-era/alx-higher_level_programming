#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

my_class = MyClass()
add_attribute(my_class, "name", "John")
print(my_class.name)

try:
    phrase = "My String"
    add_attribute(phrase, "name", "Bob")
    print(phrase.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
