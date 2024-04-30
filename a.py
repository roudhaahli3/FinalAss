from datetime import date

class Employee:
    '''class to represent an employee'''
    # Initializing the constructor
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        # all attributes are protected
        self._name = name
        self._employee_id = employee_id
        self._department = department
        self._job_title = job_title
        self._basic_salary = basic_salary
        self._age = age
        self._date_of_birth = date_of_birth
        self._passport_details = passport_details

    # Setter and Getter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Setter and Getter for employee_id
    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    # Setter and Getter for department
    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    # Setter and Getter for job_title
    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    # Setter and Getter for basic_salary
    def get_basic_salary(self):
        return self._basic_salary

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    # Setter and Getter for age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Setter and Getter for date_of_birth
    def get_date_of_birth(self):
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    # Setter and Getter for passport_details
    def get_passport_details(self):
        return self._passport_details

    def set_passport_details(self, passport_details):
        self._passport_details = passport_details

class Manager(Employee):
    '''class to represent a manager who inherits from employee'''
    # Initializing the constructor
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        # Initialize the attributes of the parent class
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self._managed_employees = []

    # Setter and Getter for managed_employees
    def get_managed_employees(self):
        return self._managed_employees

    def add_managed_employee(self, employee):
        self._managed_employees.append(employee)

class SalesManager(Manager):
    '''class to represent a Sales Manager that inherits from Manager'''
    pass

class Salesperson(Employee):
    '''class to represent a Sales person that inherits from employee'''
    # Initializing the constructor
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_manager_id):
        # Initialize the attributes of the parent class
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self._sales_manager_id = sales_manager_id

    # Setter and Getter for sales_manager_id
    def get_sales_manager_id(self):
        return self._sales_manager_id

    def set_sales_manager_id(self, sales_manager_id):
        self._sales_manager_id = sales_manager_id

class MarketingManager(Manager):
    '''class to represent a Marketing Manager that inherits from Manager'''
    pass

class Marketer(Employee):
    '''class to represent a Marketer that inherits from Employee'''
    # Initializing the constructor
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, marketing_manager_id):
        # Initialize the attributes of the parent class
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self._marketing_manager_id = marketing_manager_id

    # Setter and getter for marketing_manager_id
    def get_marketing_manager_id(self):
        return self._marketing_manager_id

    def set_marketing_manager_id(self, marketing_manager_id):
        self._marketing_manager_id = marketing_manager_id

class Accountant(Employee):
    '''class to represent an Accountant that inherits from Employee'''
    pass

class Designer(Employee):
    '''class to represent a Designer that inherits from Employee'''
    pass

class Handyman(Employee):
    '''class to represent a Handyman that inherits from Employee'''
    pass

# Testing the classes
if __name__ == "__main__":
    # Creating instances of employees
    susan_meyers = SalesManager("Susan Meyers", "47899", "Sales", "Manager", 37500, 35, date(1989, 5, 15), "AB123456")
    shyam_sundar = Salesperson("Shyam Sundar", "11234", "Sales", "Salesperson", 20000, 28, date(1996, 8, 10), "CD789012", "47899")
    joy_rogers = SalesManager("Joy Rogers", "81774", "Sales", "Manager", 24000, 30, date(1992, 3, 20), "EF345678")
    mariam_khalid = Salesperson("Mariam Khalid", "98394", "Sales", "Salesperson", 20000, 25, date(1997, 12, 5), "GH901234", "81774")

    # Adding managed employees to managers
    susan_meyers.add_managed_employee(shyam_sundar)
    joy_rogers.add_managed_employee(mariam_khalid)

    # Displaying employee details
    print("Employee Details:")
    print(f"Susan Meyers - Managed Employees: {[emp.get_name() for emp in susan_meyers.get_managed_employees()]}")
    print(f"Joy Rogers - Managed Employees: {[emp.get_name() for emp in joy_rogers.get_managed_employees()]}")
    print(f"Shyam Sundar - Manager: {shyam_sundar.get_sales_manager_id()}")
    print(f"Mariam Khalid - Manager: {mariam_khalid.get_sales_manager_id()}")
