def sum_and_pow(a1, a2):
    def my_sum():
        return a1 + a2

    def my_pow(a):
        return a * a

    return my_pow(my_sum())


print(sum_and_pow(1, 2))
print()
# 9


def make_adder(x):
    def adder(n):
        return x + n
    return adder

f = make_adder(10)
print(f(5))
print(f(-1))
print()
# 15
# 9

make_adder2 = lambda x: lambda n: x + n

f = make_adder2(10)
print(f(5))
print(f(-1))
print()
# 15
# 9