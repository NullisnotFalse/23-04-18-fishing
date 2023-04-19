import threading
import os


def foo():
    print("This is foo")


def bar():
    print("This is bar")


def baz():
    print("This is baz")


if __name__ == "__main__":
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()
