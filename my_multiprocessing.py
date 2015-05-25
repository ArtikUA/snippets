from multiprocessing import Process, Lock
from django.contrib.gis.utils.wkt import precision_wkt


def f(l, i):
    # l.acquire()
    i = 0
    for z in range(10000000):
        i -= 1
    print("OK")
    #finally:
    #    pass
        #l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        process = Process(target=f, args=(lock, num)).start()
        print(process)