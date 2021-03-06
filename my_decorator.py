def decorator1(func):
    def print_func():
        return func() * 2
    return print_func

@decorator1
def zzz():
    return 5


print(zzz())
print()


def decorator2(ololo):
    return lambda: ololo() * 2

@decorator2
def yyy():
    return 5

print(yyy())
print()