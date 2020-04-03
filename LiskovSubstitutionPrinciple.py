from abc import abstractmethod


class Animal(object):
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    @abstractmethod
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        return 4


class Mouse(Animal):
    def leg_count(self):
        return 4


class Snake(Animal):
    def leg_count(self):
        return 0


def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())


animals = [Lion("TintuMon"), Mouse("DituMole"), Snake("KittuMon")]

animal_leg_count(animals)
