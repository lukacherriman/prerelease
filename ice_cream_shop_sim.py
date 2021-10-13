import random
import math


class Simulation:
    def __init__(self):
        self.weather_list = ('storm', 'rain', 'cloud', 'partly cloudy', 'sunny')
        self.weather_base_sales = (10, 25, 75, 150, 200)
        self.day = 0

    def next_day(self):
        self.day += 1
        weather = random.randint(0, 4)
        sales = self.do_sales(weather)
        self.change_reputation()
        ice_cream_shop.resupply()
        self.display_day_end_info(weather, sales)
        ice_cream_shop.pay_rent()

    def do_sales(self, weather):
        sales = int(self.weather_base_sales[weather] * ice_cream_shop.get_rep())
        money = 0
        for sale in range(sales):
            choice = random.choice(['vanilla', 'strawberry', 'chocolate', 'raspberry'])
            ice_cream_shop.change_stock(choice)
            money += ice_cream_shop.get_stock()[choice][1]
        ice_cream_shop.increase_balance(money)
        return sales

    def display_day_end_info(self, weather_val, sales):
        balance = ice_cream_shop.get_bal()
        reputation = ice_cream_shop.get_rep()
        weather = self.weather_list[weather_val]
        stock = ice_cream_shop.get_stock()
        print(f"""
        Day: {self.day}
        Weather: {weather}
        Sales: {sales}
        New reputation: {reputation}
        New balance: {balance}
        Current stock: """)
        for flavour in stock:
            print(f" {flavour}: {stock[flavour][0]}")

    def change_reputation(self):
        change = random.choice([0, 0.05, 0.1, 0.15])
        up_down = random.randint(0, 1)
        ice_cream_shop.change_reputation(change, up_down)

    def display_menu(self):
        print(""" Press:
        1: Add additional funds
        2: Run next day
        3: Run multiple days
        q: Quit
                """)


class IceCreamShop:
    def __init__(self, balance, reputation, day_rent):
        self.balance = balance
        self.rent = day_rent
        self.reputation = reputation
        self.stock = {"vanilla": [100, 1.2, 0.4],
                      "strawberry": [200, 1.3, 0.45],
                      "chocolate": [150, 1.6, 0.5],
                      "raspberry": [100, 2, 0.6]}

    def get_rep(self):
        return self.reputation

    def get_bal(self):
        return self.balance

    def get_stock(self):
        return self.stock

    def increase_balance(self, val):
        self.balance += val

    def change_reputation(self, change, up_down):
        if up_down == 1:
            self.reputation = self.reputation + change
        else:
            self.reputation = self.reputation - change

        if self.reputation < 0.2:
            self.reputation = 0.2
        elif self.reputation > 1.2:
            self.reputation = 1.2

    def change_stock(self, choice):
        self.stock[choice][0] -= 1

    def resupply(self):
        for flavour in self.stock:
            if self.stock[flavour][0] < 40:
                self.stock[flavour][0] += 100
                self.balance -= self.stock[flavour][2] * 100

    def pay_rent(self):
        self.balance -= self.rent


# balance is any number of dollars reputation is a number between 0 and 1
simulation = Simulation()
ice_cream_shop = IceCreamShop(1000, 0.6, 10)
entry = 0
while entry != 'q':
    simulation.display_menu()
    entry = input()
    if entry == '1':
        funds = int(input('Enter the cash quantity to add: '))
        ice_cream_shop.increase_balance(funds)
    elif entry == '2':
        simulation.next_day()
    elif entry == '3':
        days = int(input('Enter the number of days: '))
        for i in range(days):
            simulation.next_day()
