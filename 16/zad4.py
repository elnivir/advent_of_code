from collections import Counter

suma = 0
with open('zad4.txt', 'r') as dane:
    for line in dane:
        temp = line.replace('-', '').replace(']', '').split('[')
        zlicz_wystapienia = Counter(temp[0][:-3])
        kod = "".join(sorted(zlicz_wystapienia, key=lambda x: (-zlicz_wystapienia.get(x), x))[:5])
        if kod == temp[1].strip():
            suma = suma + int(temp[0][-3:])

    print(suma)
