string = 'Hi there'
print('Found!!') if 'Hi' in string else print('Not found!!')
# Found!!

print()
#####################

cars = ['Audi', 'BMW', 'Tesla']

print("My favorite car are {}".format(', '.join(cars)))
# My favorite car are Audi, BMW, Tesla

print()
#####################

query = "login=Artik&password=123456&save=true"
print([pair.split('=') for pair in query.split('&')])
# [['login', 'Artik'], ['password', '123456'], ['save', 'true']]

print(dict(pair.split('=') for pair in query.split('&')))
# {'save': 'true', 'login': 'Artik', 'password': '123456'}

print({pair.split('=')[0]: pair.split('=')[1] for pair in query.split('&')})
# {'save': 'true', 'login': 'Artik', 'password': '123456'}

print()
#####################

string = "my favorite game"

print(string[:2])
# my

print(string[2:])
#  favorite game

print(string[3:11])
# favorite

print(string[:-2])
# my favorite ga

print(string[-2:])
# me



