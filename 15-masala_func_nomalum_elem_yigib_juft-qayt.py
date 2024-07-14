from os import system
system("cls")

def func(*args):
    juftlar = []
    for son in args:
        if son % 2 == 0:
            juftlar.append(son)
    return juftlar

natija = func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Juftlar = ",*natija,"\n") 
