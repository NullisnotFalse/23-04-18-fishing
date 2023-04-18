from multiprocessing import Process
import os


def foo():
    print("This is foo")


def bar():
    print("This is bar")


def baz():
    print("This is baz")


if __name__ == "__main__":
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()
