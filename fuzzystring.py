import unicodedata
from collections import UserString
from functools import total_ordering

def normalize(string):
    return unicodedata.normalize("NFD", string.casefold())


@total_ordering
class FuzzyOrderingMixin:
    def __lt__(self, other):
        return normalize(self.data) < normalize(str(other))

    def __eq__(self, other):
        return normalize(self.data) == normalize(str(other))
    
    
class FuzzyString(FuzzyOrderingMixin, UserString):
    """String case-insensitive"""

    def __add__(self, other):
        return FuzzyString(self.data + other)

    def __contains__(self, substring):
        if isinstance(substring, FuzzyString):
            substring = str(substring)
        return normalize(substring) in normalize(self.data)
