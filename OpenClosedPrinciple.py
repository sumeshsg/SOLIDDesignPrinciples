class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2


# Let’s imagine you have a store, and you give a discount of 20% to your favorite customers using this class:
# When you decide to offer double the 20% discount to VIP customers. You may modify the class like this:
# No, this fails the OCP principle.

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4


# To make it follow the OCP principle, we will add a new class that will extend the Discount.
# In this new class, we would implement its new behavior

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
