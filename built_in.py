print(bool(1))
print()

print(dict(['aa', 'bv', 'cb', 'df']))
print()

print(abs(-5))
print()

print(all([1, 1, 2, 3, 4]))
print(all([0, 1, 2, 3, 4]))
print()

print(any((0, 0, 0, 0, 0)))
print(any((0, 0, 0, 0, 1)))
print()

print(bin(7))
print()

print(chr(56))
print()

print(classmethod('abc'))
print()

code_obj = compile('print(5)', '', 'exec')
exec(code_obj)
print()

print(eval('333+333'))


class Airplane:
    pass


airplane = Airplane
setattr(airplane, 'name', 'Airbus 390')
print(getattr(airplane, 'name'))
print(airplane.name)
print(dir(airplane))
print(hasattr(airplane, 'name'))
delattr(airplane, 'name')
print(dir(airplane))
print()

print(divmod(5, 2))
print(divmod(10, 2))
print()

my_turple = (1, 2, 3, 4, 5)
print(list(enumerate(my_turple, 0)))
print(list(enumerate(my_turple, 1)))
print(list(enumerate(my_turple, 2)))
print()

print(globals())
print()

print(hash(airplane))
print()

print(help(print))
print()

print(hex(15))

print(id(airplane))
airplane.name = 'Boeing'
print(id(airplane))
print()


class Car:
    pass


car = Car()

print(issubclass(airplane, Airplane))
print(issubclass(Car, Airplane))
print()

print(len((1, 2, 3)))
print()

print(locals())
print()

print(list(map(lambda x: x / 2, (1, 1.4, 1.5, 1.6))))
print()

print(max(set((1, 1, 2, 2, 3, 3, 4, 4, 5))))
print(min(set((1, 1, 2, 2, 3, 3, 4, 4, 5))))
print()

my_map = map(lambda x: x / 2, (1, 1.4, 1.5, 1.6))
print(next(my_map))
print(next(my_map))
print(next(my_map))
print()

my_gen = (x for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) if x % 2 == 0)
print(next(my_gen))
print(next(my_gen))
print()

print(oct(10))
print()

print(ord('a'))
print()

print(pow(3, 3))
print(3 ** 3)
print()

print(next(reversed(list(x for x in range(10)))))
print()

print(repr(Airplane))
print(repr(airplane))
print()

print(round(2 / 3))
print(round(2 / 3, 0))
print(round(2 / 3, 1))
print(round(2 / 3, 2))
print(round(2 / 3, 3))
print(round(2 / 3, 4))
print(round(2 / 3, 5))
print()

print(sum((1, 2, 3, 4, 5)))
print()

print(type(1))
print(type(1.0))
print(type(0x100))
print(0x100)
print()

print(vars(airplane))
print()

t1 = [1, 2, 3]
t2 = [4, 5, 6]
print(list(zip(t1, t2)))
print()

print(5 / 2)
print(5 // 2)
print(divmod(5, 2))