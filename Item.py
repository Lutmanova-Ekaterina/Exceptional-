import csv

class Item:
    pay_rate = 0.8 #Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.prise = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        with open(f'{file}') as f:
            file_opened = csv.DictReader(f)
            for item in file_opened:
                a = item.get('name')
                b = float(item.get('price'))
                c = int(item.get('quantity'))
cls.all.append(Item(a, b, c))

    def __str__(self):
        return f'{self.__class__.__name__} + ({self.__name}, {self.price}, {self.quantity})'

Item.instantiate_from_csv('items.csv')

for item in Item.all:
    print(item)
