from threading import Thread


def count(how, n):
    #global a
    i = 0
    for z in range(10000000):
        i -= 1
    print("OK")

#a = 0

threads = []

for i in range(10):
    thread = Thread(target=count, args=(i, 10000000,))
    threads += [thread]

for thread in threads:
    print(thread)
    thread.start()

for thread in threads:
    thread.join()





#print(a)