# alternaitves: list comprehensions

airplanes = [
    ['Boeing', 400],
    ['Airbus', 300],
    ['Aeroprakt', 20],
    ['RosAvia', 10],
]

print(filter(lambda x: x[1] < 100, airplanes))
print()
# <filter object at 0x0052C390>

print(list(filter(lambda x: x[1] < 100, airplanes)))
print()
#[['Aeroprakt', 20], ['RosAvia', 10]]

##############################################

class Cars:
    name = ''
    engine = 0.0

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def __str__(self):
        return self.name


cars = (Cars('Lancer', 1.584), Cars('Impreza', 2.294), Cars('Fabia', 1.3))

for car in cars:
    print(car)
print()
# Lancer
# Impreza
# Fabia


only_powerful = filter(lambda car: car.engine > 1.4, cars)
for powerful in only_powerful:
    print(powerful)
print()
# Lancer
# Impreza


found = list(filter(lambda car: car.name == 'Lancer', cars))
lancer = found[0] if len(found) > 0 else None
print(lancer)
print()
# Lancer


found = list(filter(lambda car: car.name == 'Corolla', cars))
corolla = found[0] if len(found) > 0 else None
print(corolla)
print()
# None


