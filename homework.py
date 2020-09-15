import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now().date()
        return sum(self.records[i].amount for i in range(len(self.records)) if self.records[i].date == today)

    def get_week_stats(self):
        end_date = dt.datetime.now().date()
        begin_date = end_date - dt.timedelta(7)
        return sum(self.records[i].amount for i in range(len(self.records)) if begin_date <= self.records[i].date <= end_date)

    def get_today_stock(self):
        return self.limit - self.get_today_stats()

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 65.01
    EURO_RATE = 75.01

    @property
    def get_currencies(self):
        return {
            'usd': {'rate': self.USD_RATE, 'name': 'USD'},
            'eur': {'rate': self.EURO_RATE, 'name': 'Euro'},
            'rub': {'rate': 1, 'name': 'руб'}
        }

    def get_today_cash_remained(self, currency):

        currencies = self.get_currencies
        if currency not in currencies:
            return f'Не известная валюта {currency}'

        current_rate = currencies[currency]['rate']
        if current_rate == 0:
            return 'Курс валюты не может быть нулевым'
        current_rate_name = currencies[currency]['name']

        today_stock = self.get_today_stock()
        today_stock_currency = round(today_stock / current_rate, 2)

        if today_stock > 0:
            ret_str = f'На сегодня осталось {today_stock_currency} {current_rate_name}'
        elif today_stock == 0:
            ret_str = 'Денег нет, держись'
        else:
            ret_str = f'Денег нет, держись: твой долг - {abs(today_stock_currency)} {current_rate_name}'
        return ret_str


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stock_calories = self.get_today_stock()
        if today_stock_calories > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {today_stock_calories} кКал'
        return 'Хватит есть!'


if __name__ == "__main__":
    cash_calculator = CashCalculator(1200)
    cash_calculator.add_record(Record(amount=200, comment="кофе"))
    cash_calculator.add_record(Record(amount=800, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=300, comment="бар в Танин др", date="08.11.2019"))
    print(cash_calculator.get_today_cash_remained("rub"))
    print(cash_calculator.get_today_cash_remained("usd"))
    print(cash_calculator.get_week_stats())

    calories_calculator = CaloriesCalculator(1000)
    calories_calculator.add_record(Record(amount=500, comment="кофе"))
    calories_calculator.add_record(Record(amount=400, comment="кофе"))
    calories_calculator.add_record(Record(amount=300, comment="бар в Танин др", date="08.11.2019"))
    print(calories_calculator.get_calories_remained())
    print(calories_calculator.get_week_stats())