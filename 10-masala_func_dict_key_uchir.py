from os import system
system("cls")

def func(dct, key):
    if key in dct:
        del dct[key]
    return dct

dct = {'a': 5, 'b': 8, 'c': 4, 'd': 10}
print("Input:  ", dct)
delete = 'b'
print("\nOutput: ",func(dct, delete),"\n")