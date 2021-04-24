def add(a, b):
    return a + b

print(__name__)
print(__debug__)
# if __name__ == "__main__":
#
#     print("wykonuje testy:")

def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(-5, -10) == -15

