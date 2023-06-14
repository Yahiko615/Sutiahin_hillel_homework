from homework10.animals.mammal.mammal import Mammal


class Dolphin(Mammal):
    def __init__(self, name, habitat, num_legs, swim_speed):
        """
        Initialize a Dolphin object.

        Args:
            name (str): The name of the dolphin.
            habitat (str): The habitat where the dolphin lives.
            num_legs (int): The number of legs the dolphin has.
            swim_speed (float): The speed at which the dolphin swims.
        """
        super().__init__(name, habitat, num_legs)
        self.swim_speed = swim_speed

    def swim(self):
        """
        Simulate the dolphin swimming in the ocean.
        """
        print(f"{self.name} is swimming in the ocean.")

    def eat(self):
        """
        Simulate the dolphin eating.
        """
        print(f'Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the dolphin sleeping.
        """
        print(f'Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the dolphin living.
        """
        print(f'{self.name} is living life:')
        self.eat()
        self.sleep()
