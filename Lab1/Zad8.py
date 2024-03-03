#Napisz funkcję **reverse(napis)**, która z napisu będącego jej argumentem tworzy odwrócony napis. Przykładowo, wywołanie reverse("hello") powinno zwrócić napis "olleh".

def reverse(napis):
    #slicing
    return napis[::-1]

def reverse2(napis):
    #reverse with for loop
    result = ''
    for i in range(len(napis)-1, -1, -1):
        result += napis[i]
    return result

napis = 'hello'
print(reverse(napis))
print(reverse2(napis))