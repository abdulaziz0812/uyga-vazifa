from os import system 
system("cls")

def func (dct: dict):
    for i in dct:
        dct[i] = 0
    print("\nOutput: ",dct,"\n")

dct = {'a': 5, 'b': 8, 'c': 4, 'd': 10}
print("Input:  ", dct)
func(dct)