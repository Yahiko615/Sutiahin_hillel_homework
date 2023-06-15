from homework10.animals.animal import Animal


class Mammal(Animal):
    def __init__(self, name, habitat, num_legs):
        """
        Initialize a Mammal object.

        Args:
            name (str): The name of the mammal.
            habitat (str): The habitat where the mammal lives.
            num_legs (int): The number of legs the mammal has.
        """
        super().__init__(name, habitat)
        self.num_legs = num_legs

    def give_birth(self):
        """
        Simulate the mammal giving birth.
        """
        print(f"{self.name} is giving birth.")

    def nurse_young(self):
        """
        Simulate the mammal nursing its young.
        """
        print(f"{self.name} is nursing its young.")

    def eat(self):
        """
        Simulate the mammal eating.
        """
        print(f'Penguin Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the mammal sleeping.
        """
        print(f'Penguin Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the mammal living.
        """
        print(f'{self.name} is living life:')
        self.eat()
        self.sleep()
