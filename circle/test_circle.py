import math
import pytest

from circle import Circle


class TestCircle:

    """Tests for Circle."""

    def test_radius(self):
        circle = Circle(5)
        assert circle.radius == 5

    def test_default_radius(self):
        circle = Circle()
        assert circle.radius == 1

    def test_diameter(self):
        circle = Circle(2)
        assert circle.diameter == 4

    def test_area(self):
        circle = Circle(2)
        assert circle.area == math.pi * 4
        circle = Circle(1)
        assert circle.area == math.pi

    def test_string_representation(self):
        circle = Circle(2)
        assert str(circle) == 'Circle(2)'
        assert repr(circle) == 'Circle(2)'
        circle.radius = 1
        assert repr(circle) == 'Circle(1)'

    def test_diameter_and_area_change_based_on_radius(self):
        circle = Circle(2)
        assert circle.diameter == 4
        circle.radius = 3
        assert circle.diameter == 6
        assert circle.area == math.pi * 9

    def test_diameter_changeable_but_area_not(self):
        circle = Circle(2)
        assert circle.diameter == 4
        assert circle.area == math.pi * 4
        circle.diameter = 3
        assert circle.radius == 1.5
        with pytest.raises(AttributeError):
            circle.area = 3

    def test_no_negative_radius(self):
        circle = Circle(2)
        with pytest.raises(ValueError) as exc_info:

            circle.radius = -10

        assert "Radius cannot be negative" in str(exc_info.value)
