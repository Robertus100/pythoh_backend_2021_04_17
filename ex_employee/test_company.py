from company import Employee, PremiumEmployee


class TestEmployee:

    def test_employee_init(self):
        empl = Employee("Rafał", "Korzeniewski", 100.0)
        assert empl.first_name == "Rafał"
        assert empl.last_name == "Korzeniewski"
        assert empl.rate_per_hour == 100.0

    def test_employee_register_time(self):
        empl = Employee("Rafał", "Korzeniewski", 100.0)
        empl.register_time(5)
        assert empl.registered_time_normal == 5
        empl.register_time(10)
        assert empl.registered_time_normal == 8 + 5
        assert empl.registered_time_overtime == 2
        assert empl.registered_time_overtime == 2

    def test_employee_pay_salary(self):
        empl = Employee("Rafał", "Korzeniewski", 100.0)
        assert empl.pay_salary() == 0
        empl.register_time(5)
        assert empl.pay_salary() == 500
        assert empl.pay_salary() == 0

    def test_employee_pay_salary_overtime(self):
        empl = Employee("Rafał", "Korzeniewski", 100.0)
        empl.register_time(10)
        assert empl.pay_salary() == 8 * 100 + 2 * 2 * 100


class TestPremiumEmployee:

    def test_add_bonus(self):
        empl = PremiumEmployee("Rafał", "Korzeniewski", 100.0)
        empl.register_time(5)
        empl.give_bonus(200)

        assert empl.pay_salary() == 500 + 200
