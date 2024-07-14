from os import system 
system("cls")

def func(lst: list):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1

    max_num = max(dct, key=dct.get)
    max_count = dct[max_num]
    return max_num, max_count

lst = [2, 3, 4, 2, 2, 5, 6, 4, 3, 2, 2]
print("Input:  ",lst,"\n\nOutput: ",func(lst),"-> marta\n")