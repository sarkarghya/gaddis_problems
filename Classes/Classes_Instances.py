

class Employee:
    num = 0 #accessed each instance by Employee.num
    raise_p = 0.04
    
    def __init__(self, first, last, pay): #<--- are attributes
    # you can default these using first='Test', last='Test', pay=0 
    # never set mutables as default value types, set None and reset inside
        self.first = first #same as setting Emp.first variable
        self.last = last
        self.pay = int(pay)
        ''' # get rid of the attribute by making it a property
        self.email = f'{first}.{last}@company.com' 
        '''
        #certain variables need not be changed externally
        #such variables can be directly set by using class name
        Employee.num += 1
        
    #@property # these are methods which can be accessed as attributes
    # ie you can simply call Employee.email instead of Employee.email()
    # thereby preventing code break after external change
    @property  #access via [emp_obj].email
    def email(self): # self.email = f'{first}.{last}@company.com' 
        return f'{self.first}.{self.last}@company.com'
    '''
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter 
    def fullname(self):
        self.first, self.last = self.split(' ')
    
    @fullname.deleter 
    def fullname(self):
        self.first, self.last = None, None
    '''
    
    #'''
    def __repr__(self): #dunder repr makes object imputs readeable
        return f'Employee(\'{self.first}\', \'{self.last}\', {self.pay})'
    #'''   
    '''
    #symbols like + can be redefined using dunders
    def __add__(self, obj):
        return self.pay + obj.pay
    # try print(emp_1.pay + emp_2.pay)
    '''
   # |
   # |  These are methods
   # V
    def fullname(self): #just having self as iunput makes function empty
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay *= (1+float(self.raise_p)) 
        #notice self.raise_p can be changed externally
    
    @classmethod #Employee here is the class we are just resetting it using external code
    def set_raise_p(cls, amount):
        cls.raise_p = float(amount) #same as setting Employee.raise_p = amount externally

    @classmethod #here used to make things easier for people with similar inputs
    def from_str(cls, emp_str):
        #first, last, pay = emp_str.split('-')
        return cls(*emp_str.split('-')) #basically Employee(first, last, pay) object
    #hence class method is used as alternative constructors

    # static methods on the other hand don't pass anything automatically
    # ie. neither cls or self. These are used mostly when these variables 
    # need not be accessed form inside the definition
    '''
    @staticmethod
    def is_weekday(day):
        return day != 6 or 7
    '''

class Developer(Employee): # creates a new class by inheritance
    raise_p = 0.1
    #altering init method using inheritence
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

'''
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None): #takes list of employees as input
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp): #adds employees to list
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp): #removes employees to list
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
'''



if __name__ == "__main__":
    emp_1 = Employee('Arghya', 'Sarkar', 500) #self is not a variable
    emp_2 = Employee('Test', 'Test', 1000)
    
    print(emp_1.email) # prints Arghya.Sarkar@company.com
    print(emp_1.fullname()) # prints Arghya Sarkar
    print(Employee.fullname(emp_1)) #prints same thing
    '''
    Employee.raise_p = 0.05 #raise_p can be changed globally
    print(emp_1.raise_p) #prints 0.05
    print(emp_2.raise_p) #prints 0.05
    '''
    
    '''
    emp_1.raise_p = 0.07 #or for paricular instances 
                         #also note that is is a permanent set 
                         #and cannot be changed by global instances
    print(emp_1.raise_p) #prints 0.07
    print(emp_2.raise_p) #prints 0.05
    '''
    #namespace
    print(emp_1.__dict__) #prints dict of vals
    print(emp_2.__dict__)
    
    print(Employee.num) #prints nums of employees registered
    
    Employee.set_raise_p(0.05) #Employee.raise_p = 0.05
    print(emp_1.raise_p) #prints 0.05
    print(emp_2.raise_p) #prints 0.05
    
    emp_str_3 = 'John-Ballen-416'
    emp_3 = Employee.from_str(emp_str_3) #object name is important to future access
    print(emp_3.email) # prints Arghya.Sarkar@company.com
    print(emp_3.fullname())
    '''
    print(Employee.is_weekday(5))
    '''
    
    # inheritence
    dev_1 = Developer('Arghya', 'Sarkar', 500, 'Java') 
    dev_2 = Developer('Test', 'Test', 1000, 'Python')
    #print(help(Developer))
    print(dev_1.raise_p) #changes the raise_p in Employee class in our new class
    print(dev_1.pay) #returns 500
    dev_1.apply_raise()
    print(dev_1.pay) #returns 550
    print(isinstance(dev_1, Developer))
    print(isinstance(dev_1, Employee))
    
    #subclass
    print(dev_1.prog_lang) #return java
    print(issubclass(Developer, Employee))
    
    #dunder methods
    print(emp_1) #try after commenting code in __repr__
        # symbols like + can be redefined by __add__
    
    #magic if property
    emp_1.first = 'Asra'
    print(emp_1.first)
    print(emp_1.email)