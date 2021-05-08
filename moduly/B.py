import sys

import requests

from A import bar
from moduly import A

print(sys.argv)
print("Jestam w B")
requests.get("")


def foo(x=1):
    print("Foo z B")


class Animal:
    pass


A.bar()
foo()
bar()

x = Animal()


