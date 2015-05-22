m1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

while len(m1) > 2:
    del (m1[0])

for el in m1:
    if type(el) == list:
        while len(el) > 2:
            del (el[0])

print(m1)

m1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

newlist = [[el[i] for el in [row[-2:] for row in m1[-2:]] for i in range(0, 2)]]

print(newlist)


m1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [17, 18, 24, 25]
]


newlist = [[el[i] for el in[row[-2:] for row in m1[-2:]]] for i in range(0,2)]


print(newlist)


m1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [17, 18, 24, 25]
]


newlist = [a[-2:] for a in m1[-2:]]


print(newlist)