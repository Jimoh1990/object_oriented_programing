class Employee:
    """ Creating an employee's class """
    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_amount=5000):
        """ Creating method that raise the salary by deault and also with certain amount """
        self.annual_salary += raise_amount
