# class Bankaccount():
#     def __init__(self,account_number,balance = 0):
#         self.__account_number = account_number
#         self.__balance = balance
        
#     def deposit(self, amount):
#         self.__balance += self.amount
#         print(f"Deposited {self.amount}. current balance: {self.__balance}")
        
#     def withdraw(self, amount):
#         if self.amount > self.amount:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print (f.withdraw {amount}.current balance = {self.balance})    
            
#     def get_balance(self):
#         return self.__balance 
    
#     aK = Bankaccount("123456789", 1000) 
#     aK.deposit(500)
#     aK.withdraw(200)
#     print("Current balance:" account.get_balance)


# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks
        
#     def display_details (self):
#         print(f"Name:{self._name}")
#         print(f"marks:{self._marks}")
        
# st = Student("Jhon Doe", 90)
# st.display_details()            
            


# class Student:
#     def __init__(self, name, marks):
#      self.__name = name
#      self.__marks = marks
     
#     def display_deatils(self):
#         print(f"Name: {self.__name}")
#         print(f"Marks: {self.__marks}")
        
# st = Student("Jhon Doe", 90)
# st. display_details()    


class Vehicle:
    def __init__self(self, brand, model):
        self.brand = brand
        self.model = model
        
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year
        
    def display_details(self):
        print(f"Brand: {self.brand}")   
        print(f"Model: {self.Model}")
        print(f"year: {self.year}")              
    
    
    
    
                