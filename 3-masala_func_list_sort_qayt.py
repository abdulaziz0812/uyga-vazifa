from os import system 
system("cls")

def func(lst: list):
    return sorted(lst)

lst = [4, 2, 5, 3, 1, 6, 7, 9, 8, 10]
print("Input:  ", lst, "\n\nOutput:  ", func(lst),"\n")