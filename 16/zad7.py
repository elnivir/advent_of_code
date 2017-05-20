from re import split

with open ("zad7.txt", "r") as dane:
    for line in dane:
        tab = split("\W+", line.strip())
        print tab
        for i in tab:
            dl = len(i)/2
            if (i[dl-2:dl+2] == i[-(dl-1):-(dl+3):-1]):
                print "asd"
        print "======"