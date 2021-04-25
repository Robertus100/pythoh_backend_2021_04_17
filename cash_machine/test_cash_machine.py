import pytest

from cash_machine import CashMachine


@pytest.fixture
def cash_machine():
    return CashMachine()


class TestCashMachine:
    def test_cash_machine_not_available(self, cash_machine):
        assert not cash_machine.is_available

    def test_cash_machine_put_money(self, cash_machine):
        cash_machine.put_money([50])
        assert cash_machine.is_available

    def test_cash_machine_withdraw_money(self, cash_machine):
        cash_machine.put_money([200, 100, 100, 50])
        money = cash_machine.withdraw_money(150)
        assert money == [100, 50]

    def test_cash_machine_is_not_available_after_withdraw_all_money(self, cash_machine):
        cash_machine.put_money([200])
        cash_machine.withdraw_money(200)
        assert not cash_machine.is_available

    def test_machine_cant_withdraw(self, cash_machine):
        cash_machine.put_money([100, 100])
        assert cash_machine.withdraw_money(150) == []
