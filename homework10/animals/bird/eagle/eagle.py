from homework10.animals.bird.bird import Bird


class Eagle(Bird):
    def __init__(self, name, habitat, beak_type, wingspan):
        """
        Initialize an Eagle object.

        Args:
            name (str): The name of the eagle.
            habitat (str): The habitat where the eagle lives.
            beak_type (str): The type of beak the eagle has.
            wingspan (float): The wingspan of the eagle.
        """
        super().__init__(name, habitat, beak_type)
        self.wingspan = wingspan

    def __soar(self):
        """
        Simulate the eagle soaring in the sky.
        """
        print(f"{self.name} is soaring in the sky.")

    def eat(self):
        """
        Simulate the eagle eating.
        """
        print(f'Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the eagle sleeping.
        """
        print(f'Sleeping like a {self.name}!')

    def living_life(self):
        """
        Simulate the eagle living.
        """
        print(f'{self.name} is living life:')
        self.build_nest()
        self.lay_eggs()
        self.__soar()
