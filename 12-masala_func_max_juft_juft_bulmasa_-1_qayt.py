from os import system
system("cls")

def func(lst):
    son = -1
    for i in lst:
        if i % 2 == 0:
            if i > son:
                son = i
    
    return son

lst = [3, 7, 2, 9, 6, 4, 8]
print("Input:  ",lst,"\n\nOutput: ",f"Juft = {func(lst)}\n")