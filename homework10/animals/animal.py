from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, habitat):
        """
        Initialize an Animal object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
        """
        self.name = name
        self.habitat = habitat

    @abstractmethod
    def eat(self):
        """
        Simulate the animal eating.
        """
        pass

    @abstractmethod
    def sleep(self):
        """
        Simulate the animal sleeping.
        """
        pass
