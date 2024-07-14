from os import system 
system("cls")

def func (dct: dict):
    print("\nOutput: ",max(dct.values()),"\n")

dct = {'a': 5, 'b': 8, 'c': 4, 'd': 10}
print("Input:  ", dct)
func(dct)