

a = 10

def g():
    a = 20

    def h():
        nonlocal a
        a = 30
    h()
    print("g a: ", a)

g()
print("global a: ", a)

