from os import system
system("cls")

def func (dct: dict):
    key = set(dct.keys())
    valus = set(dct.values())
    qaytar = key.union(valus)

    return qaytar

dct = {'a': 5, 'b': 8, 'c': 4, 'd': 10}

print("Input:  ",dct,"\n\nOutput: ",func(dct),"\n")