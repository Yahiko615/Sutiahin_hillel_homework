class Employee:
    """A class representing a worker/employee."""

    def __init__(self, name, age, position, salary):
        """Initialize an Employee object.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            position (str): The position/role of the employee.
            salary (float): The salary of the employee.
        """
        self.__name = name
        self.__age = age
        self.__position = position
        self.__salary = salary

    @classmethod
    def create_employee_with_bonus(cls, name, age, position, salary, bonus):
        """Initialize an Employee object with bonus to salary.

               Args:
                   name (str): The name of the employee.
                   age (int): The age of the employee.
                   position (str): The position/role of the employee.
                   salary (float): The salary of the employee.
                   bonus (float): The salary bonus of the employee.
               """
        salary_with_bonus = salary + bonus
        return cls(name, age, position, salary_with_bonus)

    @property
    def name(self):
        """str: Get the name of the employee."""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Set the name of the employee.

        Args:
            new_name (str): The new name value.
        """
        if isinstance(new_name, str) and len(new_name) < 20:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be string of length less than 20 {type(new_name)} : {len(new_name)}')

    @property
    def age(self):
        """int: Get the age of the employee."""
        return self.__age

    @age.setter
    def age(self, new_age):
        """Set the age of the employee.

        Args:
            new_age (int): The new age value.
        """
        if isinstance(new_age, int) and 18 <= new_age < 120:
            self.__age = new_age
        else:
            raise TypeError(f'Age should be positive int more than 18 and less than 120 {type(new_age)} : {new_age}')

    @property
    def position(self):
        """str: Get the position/role of the employee."""
        return self.__position

    @position.setter
    def position(self, new_position):
        """Set the position/role of the employee.

        Args:
            new_position (str): The new position value.
        """
        if isinstance(new_position, str) and len(new_position) < 40:
            self.__position = new_position
        else:
            raise TypeError(f'Position value should be string less than 40 {type(new_position)} : {len(new_position)}')

    @property
    def salary(self):
        """float: Get the salary of the employee."""
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        """Set the salary of the employee.

        Args:
            new_salary (float): The new salary value.
        """
        if isinstance(new_salary, float) or isinstance(new_salary, int):
            self.__salary = new_salary
        else:
            raise TypeError(f'Salary value should be float or int {type(new_salary)}')

    def get_info(self):
        """Get information about the employee.

        Returns:
            str: A string that contain information about the employee.
        """
        return f"Name: {self.__name} Age: {self.__age} Position: {self.__position} Salary: {self.__salary}"

    @staticmethod
    def is_retirement_age(age):
        """Check if the given age is considered retirement age.

        Args:
            age (int): The age to check.

        Returns:
            str: String that tells if age of employee is retirement or no
        """
        retirement_age = 65
        if age >= retirement_age:
            return print(f'Age of employee is retirement = {age}')
        else:
            return print(f'Age of employee is not retirement = {age}')
