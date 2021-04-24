# import funkcje_a
a = 10
b = 5

def foo():
    "locals"
    global b
    print("foo a: ", a)
    b = 20
#
foo()
print("global b", b)


def g():
    "enclosing - non local for h"

    a = 20
    print(a)     # 20
    def h():
        print(a)  # 20
    h()

g()
print(a) # 10

# a) 10 20 20
# b) 10 20 10
# c) błą∂?