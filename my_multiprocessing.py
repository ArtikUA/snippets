from multiprocessing import Process, Lock


def f(l, i):

    try:
        for z in range(1000000):
            #l.acquire()
            print('hello world', i)
            #l.release()
    finally:
        pass


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()