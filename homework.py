import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        for i in range(len(self.records)):
            currently = dt.datetime.now().date()
            return sum(
                self.records[i].amount for i in range(len(self.records)) if self.records[i].date == currently)

    def get_week_stats(self):
        for i in range(len(self.records)):
            end_date = dt.datetime.now().date()
            begin_date = end_date - dt.timedelta(7)
            return sum(
                self.records[i].amount for i in range(len(self.records)) if
                begin_date <= self.records[i].date <= end_date)


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = self.set_date(date)

    def set_date(self, date):
        if not date:
            return dt.datetime.now().date()
        return dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 64.01
    EURO_RATE = 75.01

    @property
    def settings(self):
        return {
            'usd': {'rate': self.USD_RATE, 'name': 'USD'},
            'eur': {'rate': self.EURO_RATE, 'name': 'Euro'},
            'rub': {'rate': 1, 'name': 'руб'}
        }

    def get_today_cash_remained(self, currency):

        currencies = self.settings
        current_rate = currencies[currency]['rate']
        current_rate_name = currencies[currency]['name']

        today_stats = super().get_today_stats()
        today_stock_currency = round((self.limit - today_stats) / current_rate, 2)

        if self.limit > today_stats:
            ret_str = f'На сегодня осталось {today_stock_currency} {current_rate_name}'
        elif self.limit == today_stats:
            ret_str = "Денег нет, держись"
        else:
            ret_str = f'Денег нет, держись: твой долг - {abs(today_stock_currency)} {current_rate_name}'
        return ret_str

    def get_week_cash_remained(self, currency):

        currencies = self.settings
        current_rate = currencies[currency]['rate']
        current_rate_name = currencies[currency]['name']

        week_stats = super().get_week_stats()
        week_stock_currency = round(week_stats / current_rate, 2)

        return f'За 7 дней было потрачено {week_stock_currency} {current_rate_name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = super().get_today_stats()
        today_stock_calories = self.limit - today_stats
        if today_stats < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {today_stock_calories} кКал'
        else:
            return 'Хватит есть!'

    def get_week_stats(self):
        week_stats = super().get_week_stats()
        return f'За последние 7 дней было съедено {week_stats} кКал.'

########
# cash_calculator = CashCalculator(1000)
# cash_calculator.add_record(Record(amount=500, comment="кофе"))
# cash_calculator.add_record(Record(amount=800, comment="Серёге за обед"))
# cash_calculator.add_record(Record(amount=300, comment="бар в Танин др", date="08.11.2019"))
# print(cash_calculator.get_today_cash_remained("rub"))
# print(cash_calculator.get_today_cash_remained("usd"))
# print(cash_calculator.get_week_cash_remained("rub"))
# print(cash_calculator.get_week_cash_remained("eur"))

########
# calories_calculator = CaloriesCalculator(1000)
# calories_calculator.add_record(Record(amount=500, comment="кофе"))
# calories_calculator.add_record(Record(amount=400, comment="кофе"))
# calories_calculator.add_record(Record(amount=300, comment="бар в Танин др", date="08.11.2019"))
# print(calories_calculator.get_calories_remained())
# print(calories_calculator.get_week_stats())
