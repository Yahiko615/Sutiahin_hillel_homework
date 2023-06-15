from homework10.animals.mammal.flying_mammals.flying_mammal import FlyingMammal


class Bat(FlyingMammal):
    def __init__(self, name, habitat, num_legs, wingspan, echolocation):
        """
        Initialize a Bat object.

        Args:
            name (str): The name of the bat.
            habitat (str): The habitat where the bat lives.
            num_legs (int): The number of legs the bat has.
            wingspan (float): The wingspan of the bat.
            echolocation (bool): Whether the bat uses echolocation.
        """
        super().__init__(name, habitat, num_legs, wingspan)
        self.echolocation = echolocation

    def __navigate_with_echolocation(self):
        """
        Simulate navigating using echolocation.
        """
        print(f"{self.name} is navigating using echolocation.")

    def eat(self):
        """
        Simulate the bat eating.
        """
        print(f'Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the bat sleeping.
        """
        print(f'Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the bat living.
        """
        print(f'{self.name} is living life:')
        self.__navigate_with_echolocation()
        self.eat()
        self.sleep()
        self.nurse_young()
