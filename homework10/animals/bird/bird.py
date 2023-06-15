from homework10.animals.animal import Animal


class Bird(Animal):
    def __init__(self, name, habitat, beak_type):
        """
        Initialize a Bird object.

        Args:
            name (str): The name of the bird.
            habitat (str): The habitat where the bird lives.
            beak_type (str): The type of beak the bird has.
        """
        super().__init__(name, habitat)
        self.beak_type = beak_type

    def build_nest(self):
        """
        Simulate the bird building a nest.
        """
        print(f"{self.name} is building a nest.")

    def lay_eggs(self):
        """
        Simulate the bird laying eggs.
        """
        print(f"{self.name} is laying eggs.")

    def eat(self):
        """
        Simulate the bird eating.
        """
        print(f'Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the bird sleeping.
        """
        print(f'Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the bird living.
        """
        print(f'{self.name} is living life:')
        self.eat()
        self.sleep()
