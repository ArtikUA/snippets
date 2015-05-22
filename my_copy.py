import copy

a = 1
b = a
a = 3
print(b)
# ok


str1 = 'aaa'
str2 = str1
str1 = 'bbb'
print(str2)
# ok


list1 = [1, 2, 3]
list2 = list1
list1 = [4, 5, 6]
print(list2)
#ok


class People:
    name = ''

people1 = People()
people1.name = 'Vasia'
people2 = people1
people1.name = 'Petya'
print(people2.name)
# need copy!


people1 = People()
people1.name = 'Vasia'
people2 = copy.copy(people1)
people1.name = 'Petya'
print(people2.name)
# ok with copy!


people1 = People()
people1.name = 'Vasia'
people2 = copy.deepcopy(people1)
people1.name = 'Petya'
print(people2.name)
# ok with deep copy!


set1 = {1, 2, 3, 3}
set2 = set1
set1 = {5, 6, 7, 7}
print(set2)
# ok


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = dict1
dict1 = {'d': 4, 'e': 5, 'f': 6}
print(dict2)
# ok