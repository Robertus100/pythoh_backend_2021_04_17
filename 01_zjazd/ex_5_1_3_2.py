
def is_prime(number):
    for d in range(2, number):
        if number % d == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(121) is False
    assert is_prime(17) is True


