import pytest


class ElectricCar:

    def __init__(self, max_range):
        self.max_range = max_range
        self._traveled_distance = 0

    def drive(self, distance):
        if distance + self._traveled_distance > self.max_range:
            to_travel = self.max_range - self._traveled_distance
            self._traveled_distance = self.max_range
            return to_travel
        else:
            self._traveled_distance += distance
        return distance

    def charge(self):
        self._traveled_distance = 0


@pytest.fixture
def car100():
    return ElectricCar(100)

class TestElectricCar:
    def test_car_initialization(self, car100):
        assert car100
        assert car100.max_range == 100

    def test_car_drive_below_range(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70

    def test_car_drive_above_max_range(self):
        car = ElectricCar(100)
        assert car.drive(120) == 100

    def test_car_above_max_range_in_two_approaches(self):
        car = ElectricCar(100)
        assert car.drive(90) == 90
        assert car.drive(20) == 10

    def test_can_not_drive_when_is_discharged(self):
        car = ElectricCar(100)
        car.drive(100)
        assert car.drive(100) == 0

    def test_car_charge(self):
        car = ElectricCar(100)
        car.drive(100)
        assert car.drive(100) == 0
        car.charge()
        assert car.drive(100) == 100