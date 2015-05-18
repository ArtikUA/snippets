import re

# find one boolean
if re.match('a(.*?)c', 'abc'):
    print('found')
else:
    print('not found')
if re.match('a(.*?)c', 'ab1'):
    print('found')
else:
    print('not found')
print()
# found
# not found

# find one
x = re.search('a(.*?)c', 'abc')
print(x.group(1))
print()
# b


# find all

x = re.finditer('a(.*?)c', 'abca1c', re.MULTILINE)

for q in x:
    print(q.groups()[0])
print()
# b
# 1

# todo find multiline
x = re.finditer('''a(.*?)c''', '''ab
ca1
c''', re.MULTILINE)

for q in x:
    print(q.groups()[0])
print()
# b
# 1


# replace all
print(re.sub("a", "b", "aaasdasdgaawergageaweg"))
print()
# bbbsdbsdgbbwergbgebweg

