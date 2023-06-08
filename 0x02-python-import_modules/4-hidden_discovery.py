#!/usr/bin/python3

if __name__ == "__main__":
    
    import hidden_4

    hidden_module = dir(hidden_4)
    for module in hidden_module:
        if module[:2] != "__":
            print(module)
