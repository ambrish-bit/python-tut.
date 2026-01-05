# # 📌🔹 OOP in Python
# '''OOP(Object Oriented Programming) is a way of writing programs by creating objects.
# These objects contain data (variables) and behavior(function) together.

# in simple words:
# OOp - data + functions together'''


# # 🧱 Basic OOP Concepts in python
# # 1️⃣ Class
# '''a class is bluefprint or template for creating objects.'''
# class students:
#     pass

# # 2️⃣ Object

# '''An object is a real instance of a class.'''

# s1 = students()

# # 3️⃣ __init__ Method (Constructor)

# '''Used to initialize data when an object is created.'''

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # 4️⃣ self

# '''Refers to the current object

# Used to access variables and methods inside the class'''

# # 5️⃣ Method (Function inside a class)
# class Student:
#     def show(self):
#         print(self.name, self.age)




# class Atm:
#     # Constructor(special function)->superpower->
#     def __init__(self):
#         self.pin = ''
#         self.balance = 0
#         self.menu()

#     def menu(self):
#         user_input = input("""
#         Hii how can I help you?
#         1. Press 1 to create pin
#         2. press 2 to change pin
#         3. press 3 to check balance
#         4. press 4 to withdraw
#         5. Anything else to exit      
#         """)
#         if user_input == '1':
#           self.create_pin()
#             # create pin
#         elif user_input == '2':
#             self.change_pin()
#             # change pin   
#         elif user_input == '3':
#             self.check_balance()           
#             # check balance
#         elif user_input == '4':
#             self.withdraw()
#             # withdraw
#         else:
#             #anything to exit
#             exit()

#     def create_pin(self):
#         user_pin = input('enter your pin: ')
#         self.pin = user_pin

#         user_balance = int(input('enter balance: '))
#         self.balance = user_balance

#         print('pin created successfully')
#         self.menu()

#     def change_pin(self):
#         old_pin = input('enter old pin: ')

#         if old_pin == self.pin:
#             # let him change the pin
#             new_pin = input('enter new pin: ')
#             self.pin = new_pin
#             print('pin changed successful')
#             self.menu()
#         else:
#             print('nai karne de skta re baba,, Riskk haiii!!!')
#             self.menu()

#     def check_balance(self):
#         user_pin = input('enter your pin ')
#         if user_pin == self.pin:
#             print('your balance is ',self.balance)
#             self.menu()
#         else:
#             print('chal nikal garib!')
#             self.menu()

#     def withdraw(self):
#          user_pin = input('enter your pin')
#          if user_pin == self.pin:
#              withdraw_amount = int(input('enter withdraw amount '))
#              if withdraw_amount<=self.balance:
#                  self.balance = self.balance - withdraw_amount
#              print("withdwaw successfull, your current balance is: ",self.balance)
#              self.menu()
#          else:
#              print('kuch to jhol hai!')
#              self.menu()
         
# obj = Atm()





# ### 🔹Functions And Method
# '''when any process is inside the class then it is said to be method 
# and when a program is outside the class then it is said to functions.'''
# L = [1,2,3,4]
# b = L.append(5) # HERE this function will work inside the class so it is said to method
# a = len(L)  # HERE this function will perform outside the function so it is said to be function.
# print(a)
# print(L)




### 🧠 What is Constructor
'''📘

A constructor is a special method in a class that runs automatically when an object is created.
It is mainly used to initialize (set) values for the object, it is use for configration related code ( means the control is not have hte user.).

👉 In Python, the constructor is called __init__.

👉 Why We Use a Constructor

We use a constructor to:

Initialize object data (give starting values)

Avoid writing extra code again and again

Automatically set values when an object is created

Make objects ready to use
'''
#'''When we want to connect the data from the server or connect internet from the server
# and whatever which access we don't want to give to the customer so we use the constructor.
# '''




### 🧠 What is magic methods
'''constructors are also magic method beacuse it has a superpower and the power is unlike
other function we don't need to call that it will automatic call when we create any object.

⭐ One-Line Summary

Magic methods are special methods in Python that start and end with double underscores (__).
They let you define how objects behave with built-in operations like +, print(), len(), etc.

Magic methods let you define how objects behave with Python’s built-in functions and operators.'''







### 🧠 What is Self

'''self is object which we made to call tha functions, it is helpul to being communicate and find access with another methods and classes or variable
without self we cannot find access of another variables or methods.'''


'''📘 Simple Definition


self is a reference to the current object in a class.
It is used to access variables and methods of the same object.

🧠 Why We Use self

We use self to:

Store data inside an object

Differentiate object variables from local variables

Access class methods and variables

Make sure data belongs to the correct object

🔍 Easy Explanation

self.name → variable of current object

Without self, Python doesn’t know which object the variable belongs to'''






class Fraction:
    # parameterized constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self):    # when we put any object in print then it will automatically execute.
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):  # this magic method is use for find the addithin of two objects.
        new_num = other.den*self.num + self.den * other.num
        new_den = self.den*other.den

        return '{}/{}'.format(new_num,new_den)
    

    def __sub__(self,kuch_bhi):  # this magic method is use for find the sub between two objects.
        nya_num = kuch_bhi.den*self.num - self.den*kuch_bhi.num
        nyaa_den = self.den*kuch_bhi.num
    
        return '{}/{}'.format(nya_num,nyaa_den)
    

    def __mul__(self,dusra):
        neww_num = self.num*dusra.num
        neww_den = self.den*dusra.den

        return '{}/{}'.format(neww_num,neww_den)


    def __truediv__(self,dusra):
        newww_num = self.num*dusra.den
        newww_den = self.den*dusra.num

        return '{}/{}'.format(newww_num,newww_den)

fr1 = Fraction(3,4)
fr2 = Fraction(1,2)
print(fr1)
print(fr2)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1*fr2)
print(fr1/fr2)



# print(id(fr1))
# print(id(Fraction))