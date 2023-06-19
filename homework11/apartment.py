from home import House
from interfaces.i_taxable import ITaxable


class Apartment(House, ITaxable):
    # polymorphism
    def calculate_taxes(self):
        """
        Calculate the taxes for the apartment based on its purchase price.

        Returns:
            float: The calculated taxes for the apartment.
        """
        tax_rate = 0.2
        taxes = self.price_for_purchase * tax_rate
        return taxes


if __name__ == "__main__":
    home = Apartment("123 Some St", 2000, 100, 10000, 6)
    print(f'Your taxes is: {home.calculate_taxes()}$')
