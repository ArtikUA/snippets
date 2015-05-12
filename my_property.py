class People:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def full_name(self):
        return " с фамилией ".join([self.__first_name, self.__last_name])

    @full_name.setter
    def full_name(self, name):
        self.__first_name, self.__last_name = name.split() # name.split(None, 2)

    @full_name.deleter
    def full_name(self):
        del self.__first_name
        del self.__last_name

    def __str__(self):
        return self.full_name


person = People("Andrey", "Popp")
print(person.full_name)
print()
# Andrey с фамилией Popp

person.full_name = "Vasia Pupkin"

print(person.full_name)
# Vasia с фамилией Pupkin

print(person)
# Vasia с фамилией Pupkin

del person.full_name
#print(person)
# AttributeError: 'People' object has no attribute '_People__first_name'