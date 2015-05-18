# alternaitves: filter + lambda

airplanes = [
    ['Boeing', 400],
    ['Airbus', 300],
    ['Aeroprakt', 20],
    ['RosAvia', 10],
]

print((x for x in airplanes if x[1] < 100))
print()
# <generator object <genexpr> at 0x0078F918>

print([x for x in airplanes if x[1] < 100])
print()
# [['Aeroprakt', 20], ['RosAvia', 10]]

##############################################


class Cars:
    name = ''
    engine = 0.0

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def __str__(self):
        return self.name

    def __repl__(self):
        return self.name + self.name


cars = (Cars('Lancer', 1.584), Cars('Impreza', 2.294), Cars('Fabia', 1.3))

for car in cars:
    print(car)
print()
# Lancer
# Impreza
# Fabia


only_powerful = (car for car in cars if car.engine > 1.4)
for powerful in only_powerful:
    print(powerful)
print()
# Lancer
# Impreza


found = [car for car in cars if car.name == 'Lancer']
lancer = found[0] if len(found) > 0 else None
print(lancer)
print()
# Lancer


found = [car for car in cars if car.name == 'Corolla']
corolla = found[0] if len(found) > 0 else None
print(corolla)
print()
# None

##################################

digits = [1, 2, 3, 4, 5]
squares = [a * a for a in digits]
print(squares)
print()
# [1, 4, 9, 16, 25]


##################################

a_list = [1, 9, 8, 4]
a_list = [elem * 2 for elem in a_list]
print(a_list)
print()
# [2, 18, 16, 8]

##################################

print([i for i in range(0, 100) if i % 5 == 0])
print()
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

####################################


airplanes = [
    ['Boeing', 400],
    ['Airbus', 300],
    ['Aeroprakt', 20],
    ['RosAvia', 10],
]

airplanes_dict = {airplane[0]: airplane[1] for airplane in airplanes}
for vendor in airplanes_dict:
    print(vendor)
    print(airplanes_dict[vendor])

# Boeing
# 400
# RosAvia
# 10
# Aeroprakt
# 20
# Airbus
# 300


##################################
a_dict = {'a': 1, 'b': 2, 'c': 3}
print({value:{key, key + key} for key, value in a_dict.items()})
# {1: 'a', 2: 'b', 3: 'c'}


#######

