from abc import abstractmethod

"""
Robot call can't implement "eat()" and "drink()" method.
So Split Worker (Worker+Human)
"""


class Worker(object):
    @abstractmethod
    def do_work(self):
        raise NotImplementedError

    @abstractmethod
    def eat(self):
        raise NotImplementedError

    @abstractmethod
    def drink(self):
        raise NotImplementedError


class Employee(Worker):
    def do_work(self):
        print("Do Work")

    def eat(self):
        print("Eat Food")

    def drink(self):
        print("Drink Food")


class Robot(Worker):
    def do_work(self):
        print("Do Work")

    def eat(self):
        raise NotImplementedError

    def drink(self):
        raise NotImplementedError


####################################################

class Worker(object):
    @abstractmethod
    def do_work(self):
        raise NotImplementedError


class Human(Worker):
    @abstractmethod
    def eat(self):
        raise NotImplementedError

    @abstractmethod
    def drink(self):
        raise NotImplementedError


class Employee(Worker, Human):
    def do_work(self):
        print("Do Work")

    def eat(self):
        print("Eat Food")

    def drink(self):
        print("Drink Food")


class Robot(Worker):
    def do_work(self):
        print("Do Work")
