a = 1
b = 2

if a > b:
    print("a>b")
elif b > a:
    print("b>a")
else:
    print("=")

a = 0
while a < 10:
    if a > 5:
        print("break on {}".format(a))
        break
    a += 1
else:
    print("end")

a = 0
while a < 10:
    if a > 15:
        print("break on {}".format(a))
        break
    a += 1
else:
    print("end")

if 1 == 1 and 2 == 2:
    print("OK and")

if 1 == 1 & 2 == 2:
    print("OK &")
#NOT OK

if 1 == 2 or 2 == 2:
    print("OK or")

if 1 == 2 | 2 == 2:
    print("OK |")
#NOT OK