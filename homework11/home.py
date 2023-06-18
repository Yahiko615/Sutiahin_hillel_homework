from interfaces.i_property import IProperty


# Inheritance
class House(IProperty):
    """The Home class represents a residential home."""

    def __init__(self, address, area, price_for_rent, price_for_purchase, num_rooms):
        """
            Constructor for the Property class.

            Args:
                address (str): The address of the property.
                area (int): The area of the property.
                price_for_rent (float): The rental price of the property(monthly).
                price_for_purchase (float): The purchase price of the property.
                num_rooms (int): The number of rooms in the property.
                on_sale (bool): The property is on sale or not.

            """
        # hiding
        self.__address = address
        self.__area = area
        self.__price_for_rent = price_for_rent
        self.__price_for_purchase = price_for_purchase
        self.__num_rooms = num_rooms
        self.on_sale = True
        self._home_owner = 'Misha'

    @property
    def address(self):
        """str: Get the address of the property."""
        return self.__address

    @address.setter
    def address(self, new_address):
        """Set the address of the property.

                Args:
                    new_address (str): The new address value.
                """
        if isinstance(new_address, str) and len(new_address) < 20:
            self.__address = new_address
        else:
            raise TypeError(
                f'Address value should be string of length less than 20 {type(new_address)} : {len(new_address)}')

    @property
    def area(self):
        """str: Get the area of the property."""
        return self.__area

    @area.setter
    def area(self, new_area):
        """Set the address of the property.

                Args:
                    new_area (int): The new area value.
                """
        if isinstance(new_area, int) and len(str(new_area)) < 20:
            self.__area = new_area
        else:
            raise TypeError(
                f'Area value should be string of length less than 20 {type(new_area)} : {len(str(new_area))}')

    @property
    def price_for_rent(self):
        """str: Get the price_for_rent of the property."""
        return self.__price_for_rent

    @price_for_rent.setter
    def price_for_rent(self, new_price_for_rent):
        """Set the price_for_rent of the property.

                Args:
                    new_price_for_rent (float): The new price_for_rent value.
                """
        if isinstance(new_price_for_rent, float) and len(str(new_price_for_rent)) < 20:
            self.__price_for_rent = new_price_for_rent
        else:
            raise TypeError(
                f'Price for rent value should be float of length less than 15 {type(new_price_for_rent)} :'
                f' {len(str(new_price_for_rent))}')

    @property
    def price_for_purchase(self):
        """str: Get the price_for_rent of the property."""
        return self.__price_for_purchase

    @price_for_purchase.setter
    def price_for_purchase(self, new_price_for_purchase):
        """Set the price_for_purchase of the property.

                Args:
                    new_price_for_purchase (float): The new price_for_purchase value.
                """
        if isinstance(new_price_for_purchase, float) and len(str(new_price_for_purchase)) < 20:
            self.__price_for_purchase = new_price_for_purchase
        else:
            raise TypeError(
                f'Price for purchase value should be float of length less than 15 {type(new_price_for_purchase)} :'
                f' {len(str(new_price_for_purchase))}')

    @property
    def num_rooms(self):
        """str: Get the price_for_rent of the property."""
        return self.__num_rooms

    @num_rooms.setter
    def num_rooms(self, new_num_rooms):
        """Set the new number of rooms of the property.

                Args:
                    new_num_rooms (int): The new number of rooms value.
                """
        if isinstance(new_num_rooms, int) and len(str(new_num_rooms)) <= 3:
            self.__num_rooms = new_num_rooms
        else:
            raise TypeError(
                f'The new number of rooms value should be int of length less than 3 {type(new_num_rooms)} :'
                f' {len(str(new_num_rooms))}')

    @property
    def home_owner(self):
        """str: Get the home_owner of the property."""
        return self._home_owner

    def get_info(self):
        """Display information about the home."""
        print(f"Address: {self.address}")
        print(f"Area: {self.area} sq. ft")
        print(f"Price for rent(monthly): {self.price_for_rent}$")
        print(f"Price for purchase: {self.price_for_purchase}$")
        print(f"Number of rooms: {self.num_rooms}")
        print(f'Home owner is now {self._home_owner}')
        if self.on_sale:
            print('Property is on sale!')

    # encapsulation
    def buy(self):
        """A method for dialog with a user if he wants to buy a house"""
        user_input = input("Input your price: ")
        try:
            user_input = float(user_input)
        except ValueError:
            raise ValueError("Invalid input. Price should be a numeric value.")

        user_name = input("Input your name: ")
        try:
            if user_name.strip().isalpha():
                print(f"Thank you for your offer, {user_name}! Let's make a deal!")
        except ValueError:
            raise ValueError("Invalid input. Name should be a string value.")

        price_with_disc = self.__calc_discount()

        if user_input >= self.price_for_purchase and user_input >= price_with_disc:
            print("Lol, are you sure? This price is acceptable :D! Let's go!")
            self.is_sold(user_name)
        elif self.price_for_purchase >= user_input >= price_with_disc:
            print("Hm, fine your price is good")
            response = input(f"So you agree to the price {user_input} and want to own my house? (yes/no): ")
            if response.lower() in ["yes", "y", "+"]:
                self.is_sold(user_name)
            else:
                print("You declined the offer. The property is still on sale.")
                print(f"Home owner remains as {self._home_owner}")
        elif user_input <= self.price_for_purchase and user_input <= price_with_disc:
            print(f"Hm, your price is too low. I can offer {price_with_disc} and no less!")
            response = input("Are you willing to accept the price? (yes/no): ")
            if response.lower() in ["yes", "y", "+"]:
                self.is_sold(user_name)
            else:
                print("Deal failed. The property is still available.")
                print(f"Home owner remains as {self._home_owner}")
        else:
            raise ValueError("Your price is not acceptable.")

    def __calc_discount(self):
        """Calculate the price with a discount of 10%."""
        disc = self.__price_for_purchase * 0.1
        price_with_discount = self.__price_for_purchase - disc
        return price_with_discount

    def rent(self):
        """Method for renting the home (not yet implemented)."""
        # has not yet been implemented
        pass

    def is_sold(self, user_name):
        """Check if the home is sold and update the owner."""
        if user_name != 'Misha':
            self._home_owner = user_name
            self.on_sale = False
            print("Congratulations! You are now the owner of the property.")
            print(f"--> Home owner now is {self._home_owner}")
        else:
            print("Lol but you already own this house.")
            print("Deal failed. The property is still available.")
            print("You are home owner, do not use this method by yourself")

    def calculate_taxes(self):
        """Calculate the taxes for the given value."""
        tax_rate = 0.1
        taxes = self.__price_for_purchase * tax_rate + 450
        return print(f' Your taxes is {taxes}$')


if __name__ == "__main__":
    home = House("123 Some St", 2000, 100, 10000, 6)
    home.get_info()
    home.buy()
    home.calculate_taxes()
