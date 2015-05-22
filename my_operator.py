class People:
    age = 0

    def __add__(self, other):
        people = People
        people.age = self.age + other.age
        return people

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

people1 = People()
people1.age = 20
people2 = People()
people2.age = 30

people3 = people1 + people2
print(people3.age)

print(people1 < people2)
print(people1 <= people2)
print(people1 == people2)
print(people1 != people2)
print(people1 > people2)
print(people1 >= people2)
