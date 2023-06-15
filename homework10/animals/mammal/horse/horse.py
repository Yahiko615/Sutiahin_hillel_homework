from homework10.animals.mammal.mammal import Mammal


class Horse(Mammal):
    def __init__(self, name, habitat, num_legs, height):
        """
        Initialize a Horse object.

        Args:
            name (str): The name of the horse.
            habitat (str): The habitat where the horse lives.
            num_legs (int): The number of legs the horse has.
            height (float): The height of the horse.
        """
        super().__init__(name, habitat, num_legs)
        self.height = height

    def gallop(self):
        """
        Simulate the horse galloping at full speed.
        """
        print(f"{self.name} is galloping at full speed.")

    def eat(self):
        """
        Simulate the horse eating.
        """
        print(f'Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the horse sleeping.
        """
        print(f'Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the horse living.
        """
        print(f'{self.name} is living life:')
        self.eat()
        self.sleep()
