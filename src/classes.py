import datetime


class Operation:
    def __init__(self,
                 pk: int,
                 state: str,
                 date: str,
                 amount: str,
                 currency_name: str,
                 description: str,
                 to: str,
                 from_: str = None
                 ):
        self.pk = pk
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = self.convert_payment_data(from_) if from_ is not None else ""
        self.to = self.convert_payment_data(to)


    def convert_payment_data(self, payment_data: str) -> str:
        """
        конвертирование номера счета и карты
        :param self:
        :param payment_data:
        :return:
        """
        if payment_data.startswith('Счет'):
            return f"{payment_data[:4]} **{payment_data[-4:]}"
        return f"{payment_data[:-12]} {payment_data[-12:-10]}** **** {payment_data[-4:]}"


    def convert_payment_date(self) -> str:
        """
        конвертирование даты и приведение к заданному формату
        :param self:
        :return:
        """
        iso_date = (datetime.datetime.fromisoformat(self.date))
        return iso_date.strftime("%d.%m.%Y")


    def __lt__(self, other):
        """
        сравнение текущая меньше предыдущей даты
        :param self:
        :param other:
        :return:
        """
        return self.date < other.date


    def __gt__(self, other):
        """
        сравнение текущая больше предыдущей даты
        :param self:
        :param other:
        :return:
        """
        return self.date > other.date


    def __str__(self):
        """
        оформление вывода по образцу
        :return:
        """
        date = self.convert_payment_date()
        return (
            f"{date} {self.description}\n"
            f"{self.from_} -> {self.to}\n"
            f"{self.amount} {self.currency_name}\n"
        )
