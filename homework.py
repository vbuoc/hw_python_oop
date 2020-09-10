import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        pass

    def get_week_stats(self):
        pass

    pass


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now()):
        self.amount = amount
        self.comment = comment
        # по умолчанию Дата, но может быть передана строка 
        if type(date) == str:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')
        else:
            self.date = date
    pass


class CashCalculator(Calculator):
    # Курс валют укажите константами USD_RATE и EURO_RATE, прямо в теле класса CashCalculator.
    def get_today_cash_remained(self, currency):
        # должен принимать на вход код валюты: одну из строк "rub", "usd" или "eur". Возвращает он сообщение о
        # состоянии дневного баланса в этой валюте, округляя сумму до двух знаков после запятой (до сотых): «На
        # сегодня осталось N руб/USD/Euro» — в случае, если лимит limit не достигнут, или «Денег нет, держись»,
        # если лимит достигнут, или «Денег нет, держись: твой долг - N руб/USD/Euro», если лимит превышен.
        pass

    pass


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        # должен возвращать ответ «Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал»,
        # если лимит limit не достигнут, или «Хватит есть!», если лимит достигнут или превышен.
        pass

    pass


# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб
