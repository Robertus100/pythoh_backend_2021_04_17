
class CashMachine:

    def __init__(self):
        self._money = []

    @property
    def is_available(self):
        return bool(self._money)

    def put_money(self, bills):
        self._money.extend(bills)

    def withdraw_money(self, amount):
        money_to_withdraw = []
        for bill in sorted(self._money, reverse=True):
            if sum(money_to_withdraw) + bill <= amount:
                money_to_withdraw.append(bill)

        if sum(money_to_withdraw) != amount:
            return []

        for bill in money_to_withdraw:
            self._money.remove(bill)

        return money_to_withdraw
