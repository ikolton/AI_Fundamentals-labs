#program tworzący tablicę n na m elementów w kształcie tablicy szachowej

# tablica

n = 5
m = 5

for i in (0,n):
    for j in (0,m):
        if j%2 == 0:
            print(1)
        else:
            print(0)
    print()


