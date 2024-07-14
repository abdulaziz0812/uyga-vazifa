from os import system 
system("cls")

def func(lst: list):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1

    min_num = min(dct, key=dct.get)
    min_count = dct[min_num]
    return min_num, min_count

lst = [2, 3, 4, 2, 2, 5, 6, 4, 3, 2, 2]
print("Input:  ",lst,"\n\nOutput: ",func(lst),"-> marta\n")