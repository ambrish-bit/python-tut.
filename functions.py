# # ### 🔹🔹🔹 Functions🔹🔹🔹###
# '''A function in pyhton is a block of code that does a specific tast and can be used again and again.
# insted of writing the same code many times, uoi pit it inside a funtion and 
# call it whenever needed.'''
# '''A function is like a machine 
# if we give the input it will give some output according to the input
# '''
# # funtion is a way to make our work easier , it works on abstraction and decomposition 
# # abstraction means things are exist but does't visible
# #decomposition means many things add togather and work


# ## 🔹 Create Functions
# def is_odd(num):
#     """This function returns that the given nnumber is odd or even 
#     input - any valid positive integer
#     output - odd/even number
#     created on 25 dec 2025"""
#     if type(num) == int:
#         if num%2 != 0:
#             return 'odd'
#         else:
#             return 'even'
#     else:
#         return 'Pagal hai kya?'
# ## function
# # function_name(input)
# for i in range(1,11):
#     x = is_odd(i)
#     print(i)
#     print(x)
#     c = is_odd('hello')
#     print(c)



# ## 🔹 Parameter vs Arguments
# '''Whenever we create any funtion then it said to be parameter, but whenever we call the function
# then it is said to argument... in our upside code num is a parameter but when we call it through the 
# i then i is said to be argument.'''


# ## 🔹 Types of Arguments
# # --> Default Argument
# '''it is helpful if anyone give the sigle argument or zero argument then it will work on the basis of dafault argument.'''
# def power(a = 1, b = 1):  # IF WE GIVE VALUE TO THE PARAMETER THEN IT WILL BECOME AN ARGUMENT.
#     return a**b
# print(power(3,2))
# print(power(3))
# print(power())


# # --> Positional Argument
# print(power(3,4)) 



# ## 🔹 Documentation
# ''' by the help of that we can find the info about the function that how it works and how to access the funtion or fetch the function.'''
# print(type.__doc__)
# print(is_odd.__doc__)



# # # --> Keyword Argument
# # print(power(b = 2,a = 3)) # if we don't have any idea of positions then we can use the keyword argument 
# # '''If we have a lot of parameter and we don't have any idea about that parameter's sequence then we can use the 
# # keyword argument. it goes to the value which we mwntion for the execution and it goes the same place where we want to give the value'''

# ## 1.<> *args
# # allows us to pass a variable number of non-keywoed arguments to a function.
# def multiply(*args):
#     product = 1
#     for i in args:
#         product = product+i
#     print(args)
#     return product
    
# print(multiply(1,2,3,4,5,6,7,8,9))

# ## 2.<> **kwargs
# # **kwargs allows us to pass any number of keyword arguments.
# # Keyword argument mean that they contain a key-value pair, like a python dictionary.
# def show(**my_info):
#     for (key,value) in my_info.items():
#         print(key,'-->',value)
# print(show(name='Amb',clg = 'parul',Sem = '4th',age = '20', country= "India"))


# ## <> Points to remember using *args and **kwargs
# '''# 1.--> order of the arguments matter(normal->*args->**kwargs)
# # 2.--> The words 'args' and 'kwargs' are only a convention, you can use any name of your choice.
# '''


## 🔹 Functions in python

# ==<> Here's some questions according to the function for understand the globla and local variable concepts.

'''In a function ehich is inside the function is called the local variable , and which is outside the function is said to be 
global variable. we can call the global variable from inside the function , but we cannot call the function from the main function(global variable.)'''

# #q.1--
# def g(y):
#     print(x)
#     print(x+1) #till here it is a function which is called local variable
# x = 5
# g(x)
# print(x) # till here it is a main function ehich is called global variable.


# #q.2--
# def h(y):
#     x += 1
# x = 5
# h(x) 

# print(x)


# '''it will give error because , changing is not allow by the funtion in a global variable. and if we want to use then we have to
# apply (global) keyword.. but it is not good practice to use that.'''


# # #q.3--
# def f(x):
#     x = x+1
#     print('in f(x): x =', x)
#     return x

# x = 3
# z = f(x)
# print('in main program scope: z =', z)
# print('in main program scope: x =', x)



# ## 🔹 Nested Functions
# q.1-->
# def f():
#     def g():
#         print('inside function g')
#     g()
#     print('inside function f')
# f()


# # q.2-->
# def g(x):
#     def h():
#         x = 'abc'
#     x = x+1
#     print('in g(x): x =', x)
#     h()
#     return x
# x = 3
# z = g(x)
# print(z)



# # # q.2-->
# def g(x):
#     def h(x):
#         x= x+1
#         print('in h(x): x = ', x)
#     x = x + 1
#     print('in g(x): x = ', x)
#     h(x)
#     return x

# x = 3
# z = g(x)
# print('in main program scope: x = ', x)
# print('in main program scope: z = ', z)

# # practice -- 1
# def add(x,y):
#     def addd():
#         return  x+y
       

#     return addd()

# z = add(3,4)
# print('sum of x+y is', z)


# # practice -- 2 (find the square of num)
# def calculate_square(n):
#     def square():
#         return n**2
#     return square()
# num = calculate_square(int(input("enter a num ")))
# print(num)



# # practice -- 3 (greet your close friend)
# def greet(name):
#     def msg():
#         return "Moth*rzf4ck3r "+name
#     return msg()
# name = greet(input("Enter your name:- "))
# print(name)


# # # practice -- 4 (find simple intrest)
# def simple_intrest(p,r,t):
#     def calculate():
#         return p*r*t/100
#     return calculate()
# p = float(input('enter principle '))
# r = float(input('enter rate '))
# t = float(input('enter time '))

# si = (simple_intrest(p,r,t))
# print(si)



# # practice -- 5 (find simple intrest)
# def simple_interest(p, r, t):
#     def calculate():
#         return (p * r * t) / 100

#     return calculate()

# # taking input from user
# p = float(input("Enter Principal: "))
# r = float(input("Enter Rate: "))
# t = float(input("Enter Time: "))

# si = simple_interest(p, r, t)
# print("Simple Interest =", si)


# # # practice -- 6 (find the max of two numbers)
# def find_max(a,b):
#     def max():
#         if a>b:
#             return a
#         else:
#             return b
#     return max()

# z = find_max(3,4)
# print(z)


# # # practice -- 7  (count vowels in a list)
# def vovel_count(text):
#     def count():
#         num = 0
#         for char in text.lower():
#             if char in 'aeiou':
#                 num += 1
#         return num
#     return count()
# z = vovel_count("HIi my name is abc and i am from aeiou")
# print(z)



# # # # practice -- 7  (find the factorial of a number using nested functions.)

# def find_fact(n):
#     def fact():
#         num = 1
        
#         for i in range(1,n+1):
       
#             num *= i
#         return num
#     return fact()

# num = find_fact(int(input('enter a num')))
# print(num)  



# # # # practice -- 7 
# def calc(a,b):
#     def add():
#          a+b
#          return a+b
#     def sub():
#          a-b
#          return a-b
#     def mult():
#          a*b
#          return a*b
#     return add(), sub(), mult()
# x = int(input('ENter first num:- '))
# y = int(input('ENter second num:- '))
# add_res, sub_res, mul_res = calc(x,y)
# print(add_res)
# print(sub_res)
# print(mul_res)




# ## 🔹 Function are 1st class citizens
# # 1.--->> type and id
# '''the function store at an address which is occupied by that perticular variable if we fill that variable
# by any value it will go the same address.'''
# def square(num):
#     return num**2
# a = type(square)
# b = id(square)

# print(a)
# print(b)


# # 2.--->> reassign
# '''we can reassign the value like a=3,b=a'''
# s = square
# print(type(s))
# print(id(s))
# print(s(4))


# # 3.--->> deleting a function
# # del square
# # print(type(square))



# # 4.--->> sorting
# a = [2,4,3,1,7,8,square]
# print(a[::-1])
# print(s(a[-2]))
# print(a[-1](5))
# # print(sorted(a))
# '''if we want to check that any data is mutable or immutable then we have to use the set, if it runs then it is immutable 
# else immutable.beacuse set doesn't allow immutable data.'''
# #eg:- 
# k = {square}
# print(k)


# # 5.--->> returning a function
# def f():
#     def x(a,b):
#         return a+b
 
#     return x

# val = f()(4,7)
# print(val)




# # 6.--->> function as argument
# def func_a():
#     print('inside func_a')

# def func_b(z):
#     print('inside func_b')
#     return z()

# print(func_b(func_a))




## 🔹Benefits of using function
# --> code modularity 
'''---  means teh code goes to be sapare by that if we have any problem regariding that then we 
dont need to edit all the code we can easily goes to the branch where the code has fault then we can debug the code easily in a short time.'''

# --> code readibility
'''we can make the saveral part of our code and can use m=by other teemates , like if we have long project 
then we can distribut the code eg, login , registration etc.. which makes the code readibility.. '''


# --> code reusibility
'''means we can define the code once and use it many times.'''

