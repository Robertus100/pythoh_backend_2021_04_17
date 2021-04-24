from collections import defaultdict

def group_by(iterable, key_func=None):
    results = defaultdict(list)
    for i in iterable:
        result = key_func(i) if key_func else i
        results[result].append(i)

    return results

class TestGroupBy:
    """Tests for group_by."""

    def test_tuples_of_strings(self):
        animals = [
            ('agatha', 'dog'),
            ('kurt', 'cat'),
            ('margaret', 'mouse'),
            ('cory', 'cat'),
            ('mary', 'mouse'),
        ]
        animals_by_type = {
            'mouse': [('margaret', 'mouse'), ('mary', 'mouse')],
            'dog': [('agatha', 'dog')],
            'cat': [('kurt', 'cat'), ('cory', 'cat')],
        }
        output = group_by(animals, key_func=lambda x: x[1])

        assert output == animals_by_type

    def test_strings(self):
        words = ["Apple", "animal", "apple", "ANIMAL", "animal"]
        word_groups = {
            "apple": ["Apple", "apple"],
            "animal": ["animal", "ANIMAL", "animal"],
        }
        output = group_by(words, key_func=str.lower)
        assert output == word_groups

    def test_numbers_div_3(self):
        def mod3(n): return n % 3
        numbers = [1, 4, 5, 6, 8, 19, 34, 55]
        assert group_by(numbers, key_func=mod3) == {0: [6], 1: [1, 4, 19, 34, 55], 2: [5, 8]}


    def test_no_key_function(self):
        words = ["apple", "animal", "apple", "animal", "animal"]
        word_groups = {
            "apple": ["apple", "apple"],
            "animal": ["animal", "animal", "animal"],
        }
        output = group_by(words)
        assert output == word_groups

