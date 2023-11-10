class Worker:
    def __init__(self):
        self.employee_number = 0
        self.office_number = 0
        self.name = None
        self.birth_date = None
        self.hours_worked = 0
        self.overtime_hours = 0
        self.hourly_salary = 0.0
        self.overtime_hourly_salary = 0.0

    def get_employee_number(self):
        return self.employee_number
        
    def set_employee_number(self, employee_number):
        if not isinstance(employee_number, int):
            raise Exception("Invalid employee number")
        self.employee_number = employee_number

    def get_office_number(self):
        return self.office_number
        
    def set_office_number(self, office_number):
        if office_number < 100 or office_number > 500:
            raise Exception("Invalid office number")
        self.office_number = office_number

    def get_name(self):
        return self.name
        
   
    def set_name(self, name):
        if name == None or name == "":
            raise Exception("Invalid name")
        if "_" in name or "-" in name or "." in name:
            raise Exception("Invalid name")
        self.name = name

    def get_birth_date(self):
        return self.birth_date
        
    def set_birth_date(self, m, d, y):
        if m < 1 or m > 12:
            raise Exception("Invalid day")
        if d < 1 or d > 31:   
            raise Exception("Invalid day")
        self.birth_date = (m, d, y)
    
    def get_hours_worked(self):
        return self.hours_worked
    
    def add_hours_worked(self, hours_worked):
        if hours_worked < 0:
            raise Exception("Invalid hours worked")
        if hours_worked > 9:
            self.overtime_hours += hours_worked - 9
            self.hours_worked += 9

    def get_overtime_hours(self):
        return self.overtime_hours
    
    def set_hourly_salary(self, hourly_salary):
        self.hourly_salary = hourly_salary
        if hourly_salary < 0:
            return False
        else:
            return True
        
    def set_overtime_hourly_salary(self, overtime_hourly_salary):
        self.overtime_hourly_salary = overtime_hourly_salary
        if overtime_hourly_salary < 0:
            return False
        else: 
            return True
        
    def get_hourly_salary(self):
        return self.hourly_salary
    
    def get_overtime_hourly_salary(self):
        return self.overtime_hourly_salary
    
    def get_pay(self):
        return self.hourly_salary * self.hours_worked + self.overtime_hourly_salary * self.overtime_hours
    

    