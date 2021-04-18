def variance(mean, numbers, n):
    return sum((x - mean) ** 2 for x in numbers) / n

def mean_std(*args):
    n = len(args)
    if n == 0:
        return None, None

    X = sum(args) / n
    var = variance(X, args, n)

    sigma = var ** 0.5
    return X, sigma

def test_mean_std():
    assert mean_std() == (None, None)
    assert mean_std(1, 2) == (1.5, 0.5)
    assert mean_std(4, 4, 4, 5, 5, 5) == (4.5, 0.5)
