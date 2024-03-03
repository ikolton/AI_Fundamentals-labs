#Napisać program zamieniający napis na napis „rozstrzelony”, czyli wstawiający spacje przed napisem, pomiędzy literami i po napisie. Przykład: **'Python' → ' P y t h o n '**.

def rozstrzelony(napis):
    return ' '.join(napis)

def rostrzelony2(napis):
    for i in napis:
        print(i, end=' ')

napis = 'Python'
print(rozstrzelony(napis))
rostrzelony2(napis)