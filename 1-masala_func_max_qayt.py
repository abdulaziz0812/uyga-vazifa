from os import system 
system("cls")

def func (lst: list):
    return max(lst)

lst = [10, 20, 30, 40, 50]
print("Input:  ",lst,"\n\nOutput: ",func(lst), "\n")