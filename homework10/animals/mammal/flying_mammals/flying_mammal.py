from homework10.animals.mammal.mammal import Mammal


class FlyingMammal(Mammal):
    def __init__(self, name, habitat, num_legs, wingspan):
        """
        Initialize a FlyingMammal object.

        Args:
            name (str): The name of the flying mammal.
            habitat (str): The habitat where the flying mammal lives.
            num_legs (int): The number of legs the flying mammal has.
            wingspan (float): The wingspan of the flying mammal.
        """
        super().__init__(name, habitat, num_legs)
        self.wingspan = wingspan

    def fly(self):
        """
        Simulate the flying mammal flying.
        """
        print(f"{self.name} is flying.")

    def eat(self):
        """
        Simulate the flying mammal eating.
        """
        print(f'Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the flying mammal sleeping.
        """
        print(f'Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the flying mammal living.
        """
        print(f'{self.name} is living life:')
        self.eat()
        self.sleep()
