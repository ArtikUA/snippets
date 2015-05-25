from threading import Thread
import requests


def synchronized(lock):

    def wrap(f):
        def new_function(*args, **kw):
            lock.acquire()
            try:
                return f(*args, **kw)
            finally:
                lock.release()
        return new_function
    return wrap


def count(how, n):
    global links
    while True:
        try:
            id = list.pop(links)
        except IndexError:
            break

        link = 'http://forum.0day.kiev.ua/index.php?showtopic={}'.format(id)
        content = requests.get(link).content

        print("{} -> {}".format(how, link))
        f2 = open('bashes/{}.html'.format(id), 'wb')
        f2.write(content)

    print("OK")


a = 0

links = []

# f1 = open('links.txt', 'r')
# for line in f1:
# line = line.rstrip()
#     if line:
#         links += [line]


for i in range(400000, 401000):
    link = i
    links += [link]

print(len(links))

threads = []

for i in range(1000):
    thread = Thread(target=count, args=(i, 1000,))
    threads += [thread]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

