length = input("Enter length: ")

for i in range(1,int(length)+1):
    print("|....", end='')
print('|....|')
for i in range(int(length)+1):
    print('%5d' % i, end='')