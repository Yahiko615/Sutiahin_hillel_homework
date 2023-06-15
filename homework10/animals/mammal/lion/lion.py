from homework10.animals.mammal.mammal import Mammal


class Lion(Mammal):
    def __init__(self, name, habitat, num_legs, mane_color):
        """
        Initialize a Lion object.

        Args:
            name (str): The name of the lion.
            habitat (str): The habitat where the lion lives.
            num_legs (int): The number of legs the lion has.
            mane_color (str): The color of the lion's mane.
        """
        super().__init__(name, habitat, num_legs)
        self.mane_color = mane_color

    def roar(self) -> object:
        """
        Simulate the Lion letting out a roar.
        """
        print(f"{self.name} lets out a roar.")

    def eat(self):
        """
        Simulate the Lion eating.
        """
        print(f'Eating like a {self.name}!')

    def sleep(self):
        """
        Simulate the Lion sleeping.
        """
        print(f'Sleeping like a {self.name}!')
