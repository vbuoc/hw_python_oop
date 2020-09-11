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
                self.records[i].amount for i in range(len(self.records)) if self.records[i].date.date() == currently)

    def get_week_stats(self):
        for i in range(len(self.records)):
            end_date = dt.datetime.now().date()
            begin_date = end_date - dt.timedelta(7)
            return sum(
                self.records[i].amount for i in range(len(self.records)) if
                begin_date <= self.records[i].date.date() <= end_date)


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now()):
        self.amount = amount
        self.comment = comment
<<<<<<< HEAD
        # по умолчанию Дата, но может быть передана строка
=======
>>>>>>> Created all classes + Comment
        if type(date) == str:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')
        else:
            self.date = date


class CashCalculator(Calculator):
    USD_RATE = 74.90
    EURO_RATE = 88.80

    CURRENCIES = {
        "rub": 1.00,
        "usd": USD_RATE,
        "eur": EURO_RATE
    }

    CURRENCIES_TRANSLATE = {
        "rub": "руб",
        "usd": "USD",
        "eur": "Euro"
    }

    def get_today_cash_remained(self, currency):
        today_stats = super().get_today_stats()
        today_stock_currency = round((self.limit - today_stats) / self.CURRENCIES[currency], 2)

        if self.limit > today_stats:
            ret_str = f'На сегодня осталось {today_stock_currency} {currency}'
        elif self.limit == today_stats:
            ret_str = "Денег нет, держись"
        else:
            ret_str = f'Денег нет, держись: твой долг {today_stock_currency} {self.CURRENCIES_TRANSLATE[currency]}'
        return ret_str

    def get_week_cash_remained(self, currency):
        week_stats = super().get_week_stats()
        week_stock_currency = round(week_stats / self.CURRENCIES[currency], 2)
        return f'За 7 дней было потрачено {week_stock_currency} {self.CURRENCIES_TRANSLATE[currency]}'

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        # должен возвращать ответ «Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал»,
        # если лимит limit не достигнут, или «Хватит есть!», если лимит достигнут или превышен.
        pass

    pass


# создадим калькулятор денег с дневным лимитом 1000
#cash_calculator = CashCalculator(1000)
# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
#cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
#cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
#cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
#print(cash_calculator.get_today_cash_remained("rub"))
#print(cash_calculator.get_today_cash_remained("usd"))
# должно напечататься
# На сегодня осталось 555 руб
# сколько потрачено за неделю
#print(cash_calculator.get_week_cash_remained("rub"))
#print(cash_calculator.get_week_cash_remained("eur"))