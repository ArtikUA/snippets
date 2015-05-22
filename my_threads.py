from threading import Thread


def count(how, n):
    global a
    while n > 0:
        n -= 1
        a += 1
        print('{}\t{}'.format(how, a))
    print("OK")

a = 0

threads = []

for i in range(100):
    thread = Thread(target=count, args=(i, 100000,))
    threads += [thread]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()




print(a)