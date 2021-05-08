import pytest

from fuzzystring import FuzzyString


class TestFuzzyString:
    """Tests for FuzzyString."""

    def test_constructor(self):
        assert FuzzyString("hello")

    def test_equality_and_inequality_with_same_string(self):
        hello = FuzzyString("hello")
        assert hello == "hello"
        assert not hello != "hello"

    def test_equality_with_completely_different_string(self):
        hello = FuzzyString("hello")
        assert hello != "Hello there"
        assert not hello == "Hello there"
        assert hello != "hello there"
        assert not hello == "Hello there"

    def test_equality_and_inequality_with_different_case_string(self):
        hello = FuzzyString("hellO")
        assert hello == "Hello"
        assert not hello != "Hello"
        assert hello == "HELLO"
        assert not hello != "HELLO"

    def test_string_representation(self):
        hello = FuzzyString("heLlO")
        assert str(hello) == "heLlO"
        assert repr(hello) == repr("heLlO")

    # Testy do Bonus 1
    # zakomentuj dekorator by testy były brane pod uwagę
    @pytest.mark.xfail
    def test_other_string_comparisons(self):
        apple = FuzzyString("Apple")
        assert apple > "animal"
        assert "animal" < apple
        assert not apple < "animal"
        assert not "animal" > apple
        assert apple >= "animal"
        assert apple >= "apple"
        assert "animal" <= apple
        assert "animal" <= "animal"
        assert not apple <= "animal"
        assert not "animal" >= apple

        # Additional test between the FuzzyString objects

        warsaw = FuzzyString("Warsaw")
        wroclaw = FuzzyString("wroclaw")

        assert warsaw < wroclaw
        assert wroclaw > warsaw
        assert not warsaw > wroclaw
        assert not wroclaw < warsaw
        assert warsaw <= wroclaw
        assert warsaw <= warsaw
        assert wroclaw >= warsaw
        assert wroclaw >= wroclaw
        assert not warsaw >= wroclaw
        assert not wroclaw <= warsaw

    # Bonus 2
    @pytest.mark.xfail
    def test_string_operators(self):
        hello = FuzzyString("heLlO")
        assert hello + "!" == "helLo!"
        assert hello + "!" != "hello"
        assert "he" in hello
        assert "He!" not in hello

        # Additional test between the FuzzyString objects

        new_delhi = FuzzyString("NeW DELhi")
        new = FuzzyString("New")
        delhi = FuzzyString("Delhi")
        assert new + " " + delhi == new_delhi
        assert new + delhi != new_delhi
        assert delhi in new_delhi
        assert new in new_delhi

    # Bonus 3    
    @pytest.mark.xfail
    def test_slicing(self):
        hello = FuzzyString("heLlO")
        assert hello[-1] == "O"
        assert hello[:] == "heLlO"
        assert hello[1:3] == "eL"

    # Bonus 4
    @pytest.mark.xfail
    def test_normalizes_strings(self):
        string = FuzzyString("\u00df and ss")
        assert string == "ss and \u00df"
        string = FuzzyString("ß, ss, \uf9fb, and \u7099")
        assert string == "ss, ß, \u7099, and \uf9fb"

        accent = '\u0301'
        accented_e = FuzzyString('\u00e9')
        assert '\u0065\u0301' == accented_e
        assert accent in accented_e
