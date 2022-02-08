
from abc import ABC, abstractmethod

def Ingredient(cls, description, price):
    old_cost = cls.cost
    old_description = cls.get_description
    def cost(self):
        return old_cost(self) + price
    def get_description(self):
        return old_description(self) + " with " + description
    cls.cost = cost
    cls.get_description = get_description
    return cls

def Milk(cls):
    def wrapper():
        return Ingredient(cls, "milk", 33)
    return wrapper()

def SoyMilk(cls):
    def wrapper():
        return Ingredient(cls, "soy milk", 55)
    return wrapper()

def Mocha(cls):
    def wrapper():
        return Ingredient(cls, "mocha", 55)
    return wrapper()

def WhippedCream(cls):
    def wrapper():
        return Ingredient(cls, "whipped cream", 33)
    return wrapper()

class Beverage(ABC):
    def __init__(self,
                 description: str,
                 price: float
                 ):
        self.description = description
        self.price = price

    @abstractmethod
    def cost(self, add_in_price):
        pass

    @abstractmethod
    def get_description(self):
        pass

@Milk
class HouseBland(Beverage):
    def __init__(self):
        super().__init__("HouseBland", 100)

    def get_description(self):
        return "High quality House Bland coffee from Kenia"

    def cost(self):
        return self.price

@Milk
@WhippedCream
class DarkRoast(Beverage):
    def __init__(self):
        super().__init__("DarkRoast", 150)

    def get_description(self):
        return "Dark roast strong coffee from Equador"

    def cost(self):
        return self.price

@SoyMilk
class Decaf(Beverage):
    def __init__(self):
        super().__init__("Decaf", 80)

    def get_description(self):
        return "Decaff coffee is the healthy sort"

    def cost(self):
        return self.price

@Mocha
class Espresso(Beverage):
    def __init__(self):
        super().__init__("Espresso", 200)

    def get_description(self):
        return "You’ve never tasted such brilliant espresso"

    def cost(self):
        return self.price


house_bland = HouseBland()
print(house_bland.cost())
print(house_bland.get_description())
dark_roast = DarkRoast()
print(dark_roast.cost())
print(dark_roast.get_description())
decaf = Decaf()
print(decaf.cost())
print(decaf.get_description())



