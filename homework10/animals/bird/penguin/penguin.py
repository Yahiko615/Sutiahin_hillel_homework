from homework10.animals.bird.bird import Bird


class Penguin(Bird):
    def __init__(self, name, habitat, beak_type, swimming_ability):
        """
        Initialize a Penguin object.

        Args:
            name (str): The name of the penguin.
            habitat (str): The habitat where the penguin lives.
            beak_type (str): The type of beak the penguin has.
            swimming_ability (str): The ability of the penguin to swim.
        """
        super().__init__(name, habitat, beak_type)
        self.swimming_ability = swimming_ability

    def __slide(self):
        """
        Simulate the penguin sliding on its belly.
        """
        print(f"{self.name} is sliding on its belly.")

    def eat(self):
        """
        Simulate the penguin eating.
        """
        print(f'Penguin Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the penguin sleeping.
        """
        print(f'Penguin Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the penguin living.
        """
        print(f'{self.name} is living life:')
        self.build_nest()
        self.lay_eggs()
        self.eat()
        self.sleep()
        self.__slide()
