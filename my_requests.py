import requests

#get image from url and put in to 1.jpg
r = requests.get('http://www.sunhome.ru/UsersGallery/Cards/prazdnik_den_zemli_kartinka.jpg')
f1 = open('1.jpg', 'wb')
f1.write(r.content)

