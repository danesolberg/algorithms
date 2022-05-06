from random import random
from threading import Lock, Thread, Condition
import time


class SimpleReadWriteLock:
    def __init__(self):
        self.r_lock = Lock()
        self.r_count = 0
        self.w_lock = Lock()

    def read_acquire(self):
        self.r_lock.acquire()
        print('read acquired')
        self.r_count += 1
        if self.r_count == 1:
            self.w_lock.acquire()
        self.r_lock.release()

    def read_release(self):
        if self.r_count > 0:
            self.r_lock.acquire()
            self.r_count -= 1
            if self.r_count == 0:
                self.w_lock.release()
            print('read released')
            self.r_lock.release()

    def write_acquire(self):
        self.w_lock.acquire()
        print('write acquired')

    def write_release(self):
        self.w_lock.release()
        print('write released')


class ReadWriteLockWritePreferred:
    def __init__(self):
        self.r_lock = Condition()
        self.r_count = 0
        self.w_lock = Condition()
        self.w_processing = 0

    def read_acquire(self):
        self.r_lock.acquire()
        while self.w_processing > 0:
            self.r_lock.wait()
        print('read acquired')
        self.r_count += 1
        self.r_lock.release()

    def read_release(self):
        if self.r_count > 0:
            self.r_lock.acquire()
            self.r_count -= 1
            if self.r_count == 0:
                self.w_lock.acquire()
                self.w_lock.notifyAll()
                self.w_lock.release()
            print('read released')
            self.r_lock.release()

    def write_acquire(self):
        self.r_lock.acquire()
        self.w_processing += 1
        self.r_lock.release()
        self.w_lock.acquire()
        while self.r_count > 0:
            self.w_lock.wait()
        print('write acquired')

    def write_release(self):
        self.r_lock.acquire()
        if self.w_processing > 0:
            self.w_processing -= 1
            self.r_lock.notifyAll()
            self.w_lock.release()
        print('write released')
        self.r_lock.release()
        

class MonitorReadWriteLock:
    def __init__(self):
        self.lock = Condition()
        self.r_count = 0

    def read_acquire(self):
        self.lock.acquire()
        print('read acquired')
        self.r_count += 1
        self.lock.release()

    def read_release(self):
        if self.r_count > 0:
            self.lock.acquire()
            self.r_count -= 1
            if self.r_count == 0:
                self.lock.notifyAll()
            self.lock.release()
            print('read released')

    def write_acquire(self):
        self.lock.acquire()
        while self.r_count > 0:
            self.lock.wait()
        print('write acquired')

    def write_release(self):
        self.lock.release()
        print('write released')

    
def take_read_lock(lock: SimpleReadWriteLock):
    lock.read_acquire()
    assert lock.r_count > 0
    time.sleep(random())
    lock.read_release()

def take_write_lock(lock: SimpleReadWriteLock):
    lock.write_acquire()
    assert lock.r_count == 0
    time.sleep(random())
    lock.write_release()

if __name__ == "__main__":
    for rwlock in [
        # SimpleReadWriteLock, 
        # MonitorReadWriteLock, 
        ReadWriteLockWritePreferred,
    ]:
        lock = rwlock()
        pool = []

        for i in range(10):
            t = Thread(target=take_read_lock, args=[lock])
            t.start()
            pool.append(t)

            if i % 3 == 0:
                t = Thread(target=take_write_lock, args=[lock])
                t.start()
                pool.append(t)

        for thread in pool:
            thread.join()