def InvertDigit(a, b, c):
    a = int(str(a)[::-1])
    b = int(str(b)[::-1])
    c = int(str(c)[::-1])
    return a, b, c

sonlar = InvertDigit(68871, 54687685, 5644)
print(sonlar)
