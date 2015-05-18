#read 1.jpg and put in 2.jpg
f2 = open('2.jpg', 'wb')
f3 = open('1.jpg', 'rb')
f2.write(f3.read())


f4 = open('1.txt', 'a')
f4.write('aaaaa\n')

f5 = open('1.txt', 'r')
for line in f5:
    print(line + ' END')

