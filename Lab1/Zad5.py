# Zad. 5
#sumę,różnicę,iloczyn elementów listy.

def sum_of_list(list):
    sum = 0
    difference = 0;
    product = 1;
    for i in list:
        sum += i

    for i in list:
        difference -= i

    for i in list:
        product *= i

    return (sum, difference, product)

list = [1, 2, 3, 4, 5]
print(sum_of_list(list))