from datetime import date
from abc import ABCMeta, abstractmethod
from enum import Enum, unique

def get_today():
    return date.today()

@unique
class Sex(Enum):
    man = "M"
    woman = "W"
    androgin = "A"

class Human(metaclass=ABCMeta):
    total_count = 0

    def __init__(self, name, surname, height, weight, birth_date):
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.__children = list()
        self.sex = None
        self.mother = None
        self.father = None

    @property
    def age(self):
        return int(((get_today() - self.birth_date).days) / 365)

    @property
    def children(self):
        return self.__children

    def eat(self, dish):
        print(f"I'm eating {dish}")

    def sleep(self):
        print("I'm sleeping")

    def run(self):
        print("I'm running…")

    @abstractmethod
    def marry(self, partner, marry_partner=True):
        pass

    def add_child(self, child):
        self.__children.append(child)

class Man(Human):

    def __init__(self, name, surname, height, weight, birth_date):
        super().__init__(
            name,
            surname,
            height,
            weight,
            birth_date
        )
        self.sex = "Man"
        self.__wife = None

    @property
    def wife(self):
        return self.__wife

    def fight(self):
        print("Buhh! Bahh! Bahhh!")

    def marry(self, partner, marry_partner=True):
        self.__wife = partner
        if marry_partner:
            self.__wife.marry(self, marry_partner=False)


import datetime

class Woman(Human):

    def __init__(self, name, surname, height, weight, birth_date):
        super().__init__(
            name,
            surname,
            height,
            weight,
            birth_date
        )
        self.sex = "Woman"
        self.__husband = None

    @property
    def husband(self):
        return self.__husband

    def marry(self, partner: Man, marry_partner=True):
        self.__husband = partner
        if marry_partner:
            self.__husband.marry(self, marry_partner=False)

    def birth(self, name, height, weight, sex: Sex, father: Man):
        if sex == Sex.man:
           child = Man(
                    name,
                    father.surname,
                    height,
                    weight,
                    datetime.date.today()
            )

        elif sex == Sex.woman:
            child = Woman(
                name,
                father.surname,
                height,
                weight,
                datetime.date.today()
            )
        elif sex == Sex.androgin:
            child = Androgin(
                name,
                father.surname,
                height,
                weight,
                datetime.date.today()
            )

        child.mother = self
        child.father = father

        self.add_child(child)
        father.add_child(child)
        return child


class Androgin(Man, Woman):

    def __init__(self, name, surname, height, weight, birth_date):
        Man.__init__(
            self,
            name,
            surname,
            height,
            weight,
            birth_date)

        Woman.__init__(
            self,
            name,
            surname,
            height,
            weight,
            birth_date)
        self.sex = "Androgin from Enneade"
        self.__husband = None
        self.__wife = None

    def marry(self, partner: Human, marry_partner=True):
        if isinstance(partner, Man):
            self.__husband = partner
            if marry_partner:
                self.__husband.marry(self, marry_partner=False)
        elif isinstance(partner, Woman):
            self.__wife = partner
            if marry_partner:
                self.__wife.marry(self, marry_partner=False)


