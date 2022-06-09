from threading import Thread, Condition, Event, Semaphore

def print_in_order(n):
    def f(start, stop, jump, flag, cond, next_f):
        for i in range(start, stop+1, jump):
            cond.acquire()
            cond.wait_for(lambda: next_f[0]==flag)
            print(i)
            next_f[0] ^= 1
            cond.notify()
            cond.release()

    next_f = [0]
    cond = Condition()

    thread_even = Thread(target=f, args=(0,n,2,0, cond, next_f))
    thread_odd = Thread(target=f, args=(1,n,2,1, cond, next_f))

    thread_even.start()
    thread_odd.start()
    thread_even.join()
    thread_odd.join()


def print_in_order2(n):
    def even(n, cond):
        nonlocal even_next
        for i in range(0, n+2, 2):
            cond.acquire()
            while even_next is False:
                cond.wait()
            print(i)
            even_next = False
            cond.notify()
            cond.release()

    def odd(n, cond):
        nonlocal even_next
        for i in range(1, n+1, 2):
            cond.acquire()
            while even_next is True:
                cond.wait()
            print(i)
            even_next = True
            cond.notify()
            cond.release()

    cond = Condition()
    even_next = True

    thread_odd = Thread(target=odd, args=(n, cond))
    thread_even = Thread(target=even, args=(n, cond))

    thread_odd.start()
    thread_even.start()
    thread_odd.join()
    thread_even.join()


def print_in_order_Event(n):
    def even(n, do_odd, do_even):
        for i in range(0, n+2, 2):
            do_even.wait()
            print(i)
            do_even.clear()
            do_odd.set()

    def odd(n, do_odd, do_even):
        for i in range(1, n+1, 2):
            do_odd.wait()
            print(i)
            do_odd.clear()
            do_even.set()

    do_odd = Event()
    do_even = Event()
    do_even.set()

    thread_odd = Thread(target=odd, args=(n, do_odd, do_even))
    thread_even = Thread(target=even, args=(n, do_odd, do_even))

    thread_odd.start()
    thread_even.start()
    thread_odd.join()
    thread_even.join()


def print_in_order_semaphore(n):
    semEven = Semaphore(1)
    semOdd = Semaphore(0)

    def even(n, semEven, semOdd):
        for i in range(0, n+2, 2):
            semEven.acquire()
            print(i)
            semOdd.release()

    def odd(n, semEven, semOdd):
        for i in range(1, n+1, 2):
            semOdd.acquire()
            print(i)
            semEven.release()

    thread_odd = Thread(target=odd, args=[n, semEven, semOdd])
    thread_even = Thread(target=even, args=[n, semEven, semOdd])

    thread_odd.start()
    thread_even.start()
    thread_odd.join()
    thread_even.join()


if __name__ == "__main__":
    print_in_order_semaphore(20)