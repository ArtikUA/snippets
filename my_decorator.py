def decorator1(func):
    def print_func():
        return func() * 2
    return print_func

@decorator1
def zzz():
    return 5


print(zzz())