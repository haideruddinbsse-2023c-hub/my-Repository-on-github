# class cecos:
#     def __(self):
#         self.__name= 'yaseen'
#         self.__id= 123
#         def setdate(self):
#             self.__name =input("name")
#             self.__id =int (input("id"))
            
#     def getdata(self):
#         print(f"name {self.__name} id {self.__id}")    
        
# C1 = cecos()
# C1.getdata()        

# class cecosian:
#     def __init__(self):
#         self.name = "abc"
#         self.id = 123
#         self.adress = "abc"
#         self.contact = 123
#         self.qualification = "ab"
        
#     def __setdata(self):
#         self.name = input("Name")
#         self.id = 123
#         self.adress = "abc"
#         self.contact = 123
#         self.qualification = "ab"


# 1: 

# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited {amount}. Current balance: {self.__balance}")

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient balance!")
#         else:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. Current balance: {self.__balance}")

#     def get_balance(self):
#         return self.__balance

# account = BankAccount("123456789", 1000)
# account.deposit(500)
# account.withdraw(200)
# print("Current balance:", account.get_balance())


# 2: 

# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     def display_details(self):
#         print(f"Name: {self.__name}")
#         print(f"Marks: {self.__marks}")

# student = Student("John Doe", 90)
# student.display_details()


# 3: 

# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary

#     def update_salary(self, new_salary):
#         self.__salary = new_salary

#     def display_salary(self):
#         print(f"Salary: {self.__salary}")

# employee = Employee("Jane Doe", 50000)
# employee.display_salary()
# employee.update_salary(60000)
# employee.display_salary()


#  4: 

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model)
#         self.year = year

#     def display_details(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

# car = Car("Toyota", "Corolla", 2020)
# car.display_details()


# 5: 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_number}")

student = Student("John Doe", 20, "1234")
student.display_details()


#  6: 

# class Grandparent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Parent(Grandparent):
#     def __init__(self, name, age, child_name):
#         super().__init__(name, age)
#         self.child_name = child_name

# class Child(Parent):
#     def __init__(self, name, age, child_name, grandchild_name):
#         super().__init__(name, age, child_name)
#         self.grandchild_name = grandchild_name

#     def display_details(self):
#         print(f"Grandparent: {self.name}")
#         print(f"Parent: {self.child_name}")
#         print(f"Child: {self.grandchild_name}")

# child = Child("Grandma", 60, "Mom", "Me")
# child.display_details()


# 7: 

# class Device:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Computer(Device):
#     def __init__(self, brand, model, processor):
#         super().__init__(brand, model)
#         self.processor = processor

# class Laptop(Computer):
#     def __init__(self, brand, model, processor, ram):
#         super().__init__(brand, model, processor)
#         self.ram = ram

#     def display_details(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Processor: {self.processor}")
#         print(f"RAM: {self.ram}")

# laptop = Laptop("Dell", "Inspiron", "Intel Core i5", "8GB")
# laptop.display_details()


#  8:
# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):
#     def __init__(self, name, employee_id):
#         super().__init__(name)
#         self.employee_id = employee_id

# class Manager(Employee):
#     def __init__(self, name, employee_id, department):
#         super().__init__(name, employee_id)
#         self.department = department

#     def display_name(self):
#         print(f"Manager's Name: {self.name}")

# manager = Manager("John Doe", "E123", "HR")
# manager.display_name()


#  9: 
# class Academics:
#     def __init__(self, subject):
#         self.subject = subject

# class Sports:
#     def __init__(self, sport_name):
#         self.sport_name = sport_name

# class Student(Academics, Sports):
#     def __init__(self, name, subject, sport_name):
#         Academics.__init__(self, subject)
#         Sports.__init__(self, sport_name)
#         self.name = name

#     def display_details(self):
#         print(f"Student Name: {self.name}")
#         print(f"Academic Subject: {self.subject}")
#         print(f"Sport Name: {self.sport_name}")


# student = Student("Jane Doe", "Mathematics", "Cricket")
# student.display_details()


#  10:
# class Camera:
#     def __init__(self, camera_resolution):
#         self.camera_resolution = camera_resolution

# class MusicPlayer:
#     def __init__(self, music_format):
#         self.music_format = music_format

# class Smartphone(Camera, MusicPlayer):
#     def __init__(self, brand, camera_resolution, music_format):
#         Camera.__init__(self, camera_resolution)
#         MusicPlayer.__init__(self, music_format)
#         self.brand = brand

#     def display_features(self):
#         print(f"Brand: {self.brand}")
#         print(f"Camera Resolution: {self.camera_resolution}")
#         print(f"Music Format: {self.music_format}")


# smartphone = Smartphone("Apple", "12MP", "MP3")
# smartphone.display_features()

              