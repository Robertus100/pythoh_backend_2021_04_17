def is_palindrome(text):
    """
    Check if text is palindrome

    >>> is_palindrome("Co mi dał duch – cud, ład i moc.")
    True

    >>> is_palindrome("Ala ma kota")
    False

    :param text: str
    :return: bool
    """

    signs = [sign for sign in text.lower() if sign.isalnum()]
    return signs == signs[::-1]


# def is_palindrome(test: str) -> bool:
#     ...

#
#
# def test_is_palindrome():
#     assert is_palindrome("Co mi dał duch – cud, ład i moc.") is True
#     assert is_palindrome("Jeż leje lwa, paw leje lżej.") is True
#     assert is_palindrome("Ile Roman ładny dyndał na moreli?") is True
#     assert is_palindrome("Ada bąki piką bada.") is True
#
#     assert is_palindrome("Ala ma kota") is False

if __name__ == "__main__":
    import doctest
    doctest.testmod()