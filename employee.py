import json
import logging

logging.basicConfig(level=logging.INFO)


def load(file_name="employees.json"):
    logging.info("Odczyt z bazy")
    try:
        with open(file_name) as f:
            try:
                data = json.load(f)
                data = [Employee(**d) for d in data]
            except json.decoder.JSONDecodeError:
                data = []
    except FileNotFoundError:
        data = []
    return data


def save(data, file_name="employees.json"):
    logging.info("Zapis do bazy")
    with open(file_name, 'w') as f:
        data = [d.__dict__ for d in data]
        json.dump(data, f)


class Employee:
    id = 1

    def __init__(self, first_name, last_name, b_year, rate_per_hour, registered_normal_hours=0,
                 registered_overtime_hours=0, id=None):
        if not id:
            self.id = Employee.id
            Employee.id += 1
        else:
            self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.b_year = b_year
        self.registered_normal_hours = registered_normal_hours
        self.registered_overtime_hours = registered_overtime_hours

    def register_time(self, hours):
        if hours <= 8:
            self.registered_normal_hours += hours
        else:
            self.registered_normal_hours += 8
            self.registered_overtime_hours += hours - 8

    def pay_salary(self):
        salary = (self.registered_normal_hours * self.rate_per_hour +
                  self.registered_overtime_hours * self.rate_per_hour * 2)
        self.registered_normal_hours = 0
        self.registered_overtime_hours = 0
        return salary

    def __str__(self):
        return f"- [{self.id}] {self.first_name} {self.last_name} - rok: {self.b_year}, stawka: {self.rate_per_hour} PLN, " \
               f"godziny: {self.registered_normal_hours}, nadgodziny: {self.registered_overtime_hours}"


def command(employees):
    if employees:
        c = input("Co chcesz zrobić? [d - dodaj, w - wypisz, p-wypłać, r-rejestracja czasu]")
    else:
        c = input("Co chcesz zrobić? [d - dodaj, w - wypisz]")

    return c


def add(employees):
    imie = input("imie: ")
    nazwisko = input("nazwisko: ")
    rok_ur = input("rok urodzenia")
    stawka = int(input("stawka: "))
    godziny = int(input("Godziny: "))

    empl = Employee(first_name=imie, last_name=nazwisko, b_year=rok_ur, rate_per_hour=stawka)
    empl.register_time(godziny)

    employees.append(empl)
    return employees


employees = load()


while True:
    c = command(employees)
    if c == 'd':
        employees = add(employees)
        save(employees)
    elif c == "w":
        print("Pracownicy:")
        for e in employees:
            print(e)
    elif c == 'p':
        e_id = int(input("id użytkownika: "))
        e = employees[e_id - 1]
        print(e.pay_salary())
        save(employees)
    elif c == 'r':
        e_id = int(input("id użytkownika: "))
        e = employees[e_id - 1]
        hours = int(input("Ile godzin: "))
        e.register_time(hours)
        save(employees)
    else:
        logging.info("Koniec")
        break