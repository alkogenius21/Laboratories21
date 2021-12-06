# количество учеников
n=int(input())

lang=[]
#создание списков
for _ in range(n):
    k = int(input())
    buff=set()
    for _ in range(k):
        buff.add(input())      
    lang.append(buff)
#объединение списков 
unic = set.union(*lang)
intersec = set.intersection(*lang)
#вывод результата
print(len(intersec), '\n'.join(sorted(intersec)), len(unic), '\n'.join(sorted(unic)), sep='\n')