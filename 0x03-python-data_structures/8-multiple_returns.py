#!/usr/bin/python3
zero = 0
def multiple_returns(sentence):
    
    if sentence == "":
        return (zero, None)
    return (len(sentence), sentence[zero])

