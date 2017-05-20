from collections import Counter

tab_liter = 8 * [""]
kod = ""

with open('zad6.txt', 'r') as dane:
    for line in dane:
        tab_liter = [x+y for x, y in zip(tab_liter, line)]

for i in tab_liter:
    kod = kod + Counter(i).most_common()[0][0]


print(kod)
