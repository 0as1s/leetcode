from threading import Lock
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_1 = Lock()
        self.lock_2 = Lock()
        self.lock_2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.lock_1.acquire()
            printFoo()
            self.lock_2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_2.acquire()
            printBar()
            self.lock_1.release()
