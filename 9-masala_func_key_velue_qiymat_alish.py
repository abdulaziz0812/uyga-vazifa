from os import system
system("cls")

def func (dct: dict):
    natija = {j: i for i, j in dct.items()}
    print("\n\nOutput: ",natija,"\n")
   

dct = {'a': 5, 'b': 8, 'c': 4, 'd': 10}
print("Input:  ", dct)
func(dct)