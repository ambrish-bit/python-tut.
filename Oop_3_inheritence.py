# # ✨ Class Relationships

# # 🔹 Aggregation
# # 🔹 Inheritence


# #  👉 Aggregation
# '''--> Relationship between Classes <-- when any class is part of another class, like a resturent has menu or customer info has 
# details like ,neme, gender, age , address so here we cannot define the address in the same class that's
# why we have to use another class foe the address and that is called aggregation which is thw 
# part of another class
# in simple words --> when any class is part of another class or relate with another class then 
# it will said to be aggregation.'''
# #example
# class Customer:
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address

#     def print_address(self):
#         print(self.address.get_city(),self.address.pin,self.address.state)
    
#     def edit_profile(self,name,new_city,new_pin,new_state):
#         self.name = name
#         self.address.edit_address(new_city,new_pin,new_state)


# class Address:
#     def __init__(self,city,pin,state):
#         self.__city = city
#         self.pin = pin
#         self.state = state

#     def get_city(self):
#         return self.__city
    
#     def edit_address(self,new_city,new_pin,new_state):
#         self.__city = new_city
#         self.pin = new_pin
#         self.state = new_state

    
# '''if there's a diamond symbol in the diagram that means it is a symbol of aggregation
# '''
# add1 = Address('GKP',273152,'UP')
# cust = Customer('Amb','male',add1)
# cust.print_address()


# cust.edit_profile('Amb','Vadodra',391760,'Gujrat')
# cust.print_address()

 







# ###  👉  Inheritence
# '''Inheritence means redundency means once if fefine something then use it for multiple times.
# it means resusability, once make the class and use that other neccessary place, if two classes
# has same method there we can use inheritence to make our code smooth and easy to usable multiple time.'''
 

# #parent class
# class User:
#     def __init__(self):
#         self.name = 'Amb'

#     def login(self):
#         print('login')


# #child class
# class Student(User):
#     pass
# ## once we use the constructor in the parent class then we shouldn't have to use it in the child class.

#     def enroll(self):
#         print('enroll into the course')

# u = User()
# s = Student()

# '''if there is triangle in the diagramm it means it is a symbol of inheritence.'''

# print(s.name)
# print(s.login())
# print(s.enroll())


###--> What is inherited? <--
# 🔹 Constructor
# 🔹 Non Private Attributes
# 🔹 Non Private Methods


# ###<> Constructor example
# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     pass

# s = Smartphone(20000,"Apple",13)
# s.buy




### If it is alredy defined in the children class then the object will not goes for the parent class that;s why attribute will not intitalize
# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print('Buying a phone')

# class Smartphone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print("Inside Smartphone constructor")

# s = Smartphone("Android",4)
# s.buy
# s.brand








# ## Child can't access private member of the class

# class Phone:
#     def __init__(self,price,brand,camera):
#         print('Inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

        ##getter
#     def show(self):
#         print(self.__price)

# class Smartphone(Phone):
#     def check(self):
#         print(self.__price)


# s = Smartphone(20000,"Apple",13)
# print(s.brand)
# # s.check()
 # s.show()






# #### <> <> <> .
# class Parent:
#     def __init__(self,num):
#         self.__num = num

#     def get_num(self):
#         return self.__num
    
# class Child(Parent):
    
#     def show(self):
#         print('This is in child class')


# son = Child(100)
# print(son.get_num)
# son.show()





# #### <> <> <> .
class Parent:
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):

    def __init__(self,val,num):
        self.__val = val
        self.__num = num
        
    def get_val(self):
        return self.__val

        
    
son = Child(100,10)
# print('parent: Num:',son.get_num())
print('Childs: val:',son.get_val())















# class Customer:
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address


#     def print_address(self):
#         print(self.address.get_city(),self.address.pincode,self.address.state)

#     def edit_profile(self,new_name,new_city,new_pincode,new_state):
#         self.name = new_name
#         self.address.edit_address(new_city,new_pincode,new_state)

# class Address:
#     def __init__(self,city,pincode,state):
#         self.__city = city
#         self.pincode = pincode
#         self.state = state

#     def get_city(self):
#         return self.__city
    
#     def edit_address(self,new_city,new_pincode,new_state):
#         self.__city = new_city
#         self.pincode = new_pincode
#         self.state = new_state
     

# add1 = Address('GKP',273152,'UP')
# cust = Customer('Amb','male',add1)
# cust.print_address()


# cust.edit_profile('Amb','Vadodra',391760,'Gujrat')
# cust.print_address()

 