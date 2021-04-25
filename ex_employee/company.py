class Employee:

    def __init__(self, first_name, last_name, rate_per_hour):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.registered_time_normal = 0
        self.registered_time_overtime = 0

    def register_time(self, time):
        if time <= 8:
            self.registered_time_normal += time
        else:
            self.registered_time_normal += 8
            self.registered_time_overtime += time - 8

    def pay_salary(self):
        salary = (
                self.registered_time_normal * self.rate_per_hour +
                self.registered_time_overtime * self.rate_per_hour * 2
        )
        self.registered_time_overtime = 0
        self.registered_time_normal = 0
        return salary

class PremiumEmployee(Employee):

    def __init__(self, first_name, last_name, rate_per_hour):
        super().__init__(first_name, last_name, rate_per_hour)
        self.bonuses = 0

    def give_bonus(self, bonus):
        self.bonuses += bonus

    def pay_salary(self):
        base_salary = super().pay_salary()
        salary = base_salary + self.bonuses
        self.bonuses = 0
        return salary