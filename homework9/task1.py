class Company:
    """A class representing a company."""

    def __init__(self, name, industry, location, employee_count):
        """Initialize a Company object.

        Args:
            name (str): The name of the company.
            industry (str): The industry the company operates in.
            location (str): The location of the company.
            employee_count (int): The number of the employees.
        """
        self.__name = name
        self.__industry = industry
        self.__location = location
        self.__employee_count = employee_count

    @property
    def name(self):
        """str: Get the name of the company."""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Set the name of the company.

        Args:
            new_name (str): The new name value.
        """
        if isinstance(new_name, str) and len(new_name) < 20:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be string of length less than 20 {type(new_name)} : {len(new_name)}')

    @property
    def industry(self):
        """str: Get the industry the company operates in."""
        return self.__industry

    @industry.setter
    def industry(self, new_industry):
        """Set the industry of the company.

        Args:
            new_industry (str): The new name value.
        """
        if isinstance(new_industry, str) and len(new_industry) < 30:
            self.__industry = new_industry
        else:
            raise TypeError(
                f'Industry should be string of length less than 30 {type(new_industry)} : {len(new_industry)}')

    @property
    def location(self):
        """str: Get the location of the company."""
        return self.__location

    @location.setter
    def location(self, new_location):
        """Set the location of the company.

        Args:
            new_location (str): The new name value.
        """
        if isinstance(new_location, str) and len(new_location) < 20:
            self.__location = new_location
        else:
            raise TypeError(
                f'Location should be string of length less than 20 {type(new_location)} : {len(new_location)}')

    @property
    def employee_count(self):
        """str: Get the count of the employees of the company."""
        return self.__employee_count

    @employee_count.setter
    def employee_count(self, new_employee_count):
        """Set the count of the employees of the company.

        Args:
            new_employee_count (int): The new count of the employees.
        """
        if isinstance(new_employee_count, int):
            self.__employee_count = new_employee_count
        else:
            raise TypeError(f'Number of the employees should be int {type(new_employee_count)}')

    def get_info(self):
        """Get information about the company.

        Returns:
            str: A string containing information about the company.
        """
        return f"Company Name: {self.__name} Industry: {self.__industry} Location: {self.__location} Number of the " \
               f"employees: {self.__employee_count}"

    @staticmethod
    def is_large_company(num_of_the_employees):
        """Check if the company is considered a large company based on the number of employees.

        Args:
            num_of_the_employees (int): The number of employees in the company.

        Returns:
            bool: True if the company is considered large, False otherwise.
        """
        large_company = 1000
        return num_of_the_employees >= large_company

    @classmethod
    def create_from_dict(cls, company_dict):
        """Create a Company object from a dictionary.

        Args:
            company_dict (dict): A dictionary containing company information.

        Returns:
            Company: A Company object created from the dictionary.
        """
        name = company_dict.get('name')
        industry = company_dict.get('industry')
        location = company_dict.get('location')
        employee_count = company_dict.get('employee_count')
        return cls(name, industry, location, employee_count)


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


if __name__ == "__main__":
    comp = Company('Blizzard', 'Games', 'USA', 10000)
    company_d = {
        "name": "Blizzard",
        "industry": "Games",
        "location": "USA",
        "employee_count": 10000

    }
    comp_d = Company.create_from_dict(company_d)
    comp.name = 'Marina'
    comp.industry = 'Bullying'
    comp.location = 'Ukraine'
    comp.employee_count = 1500
    if Company.is_large_company(comp.employee_count):
        print(f'{comp.name} is large company!')
    else:
        print(f'{comp.name} is not a large company!')

    check_info = comp.get_info()
    print(check_info)
    check_info_with_bonus = comp_d.get_info()
    print(check_info_with_bonus)

    misha = Employee('Misha', 21, 'QA', 1000.50)
    misha_with_bonus = Employee.create_employee_with_bonus('Misha', 21, 'QA', 1000.50, 1000)
    misha.name = 'Marina'
    misha.age = 22
    misha.position = 'QAA'
    misha.salary = 1500
    Employee.is_retirement_age(misha.age)
    check_info = misha.get_info()
    print(check_info)
    check_info_with_bonus = misha_with_bonus.get_info()
    print(check_info_with_bonus)
