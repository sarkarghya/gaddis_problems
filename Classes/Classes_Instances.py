

class Employee:
    raise_p = 0.04
    
    def __init__(self, first, last, pay): #<--- are attributes
    # you can initalize these using first='Test', last='Test', pay=0 
        self.first = first #same as setting Emp.first variable
        self.last = last
        self.pay = int(pay)
        self.email = f'{first}.{last}@company.com'
        
    def fullname(self): #just having self as iunput makes function empty
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay *= (1+float(self.raise_p))

emp_1 = Employee('Arghya', 'Sarkar', 500) #self is not a variable
emp_2 = Employee('Test', 'Test', 1000)

if __name__ == "__main__":
    print(emp_1.email) # prints Arghya.Sarkar@company.com
    print(emp_1.fullname()) # prints Arghya Sarkar
    print(Employee.fullname(emp_1))
    
    print(emp_1.pay)
