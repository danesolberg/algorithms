from threading import Thread, Lock, Condition

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
    lock = Lock()
    cond = Condition(lock)

    thread_even = Thread(target=f, args=(0,n,2,0, cond, next_f))
    thread_odd = Thread(target=f, args=(1,n,2,1, cond, next_f))

    thread_even.start()
    thread_odd.start()
    thread_even.join()
    thread_odd.join()


if __name__ == "__main__":
    print_in_order(20)