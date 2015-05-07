def f1(x):
    yield x
    x = 5
    yield x
    x /= 2
    yield x
    x = '111'
    yield x


counter = f1(2)

for f in counter:
    print(f)
# 2
# 5
# 2.5
# 111

#############################################

def fib(maximum):
    a, b = 0, 1
    while a < maximum:
        yield a
        a, b = b, a + b

print(list(fib(100)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
