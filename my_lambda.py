# alternative: list comprehensions
digits = [1, 2, 3, 4, 5]

squares = list(map(lambda a: a * a, digits))
print(squares)
# [1, 4, 9, 16, 25]



