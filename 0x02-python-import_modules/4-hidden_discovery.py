#!/usr/bin/python3

if __name__ == "__main__":
    
    import hidden_4

     hidden_module= dir(hidden_4)
    for names in hidden_module:
        if names[:2] != "__":
            print(names)

