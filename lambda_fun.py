## 📌🔹 Lambda Function (Python)

'''A lambda function is a small, anonymaous function in python that is
written in 
one single line.
it is used for short and simple operations.'''


## 📘 Explanation
#1.--> A lambda function does not have a name
#2.--> it is written using the keyword lambda
#3.--> it can take any number of arguments
#4.--> it can have only one expression
#5.--> The resilt is returned automaticall (no return keyword)




## 🧱 Syntax
# lambda arguments : expression

## 📘 Diff between lambda vs a Normal Function
#1.--> No name
#2.-->lambda has no return value(infact, return a function)
#3.--> lambda is written in 1 line
#4.--> not reusable
#5.--> They are used with Higher Order Functions


# # find square of number using lambda functions
# a = lambda x: x**2
# print(a(2)) 


# # find sum of two numbers using lambda functions
# b = lambda x,y: x+y
# print(b(5,8))


# # Chech if a string has 'h'
# c = lambda str: 'h' in str
# print(c('hello'))


# # find even or odd number using lambda function
# d = lambda x: 'even' if x%2==0 else 'odd'
# print(d(7))




# ## 🧱 Higher Order Function 
# '''if a function returns another function that it is said to be higher order function.
# else,, if a function return another function then it is said to be higher order function
# else,,,if a function recieve another function inside the input then it is also said to be higher order function. '''


# # # 1. 🔹 Map
# # square the items of a list
# a = list(map(lambda x:x**2,[1,2,3,4,5,6]))
# print(a)


# # odd/even labelling of list items
# l = [2,3,4,5,6,7]
# b = list(map(lambda x: 'even' if x%2==0 else 'odd',l))
# print(b)


# # fetch names from a list of dict

# comapny_info = [
#     {
#       'name':'raj',
#       'gender':'male',
#       'age': 20,
#       'add':'Pip' 
#     },
#     {
#         'name':'Dpk',
#         'gender':'male',
#         'age':21,
#         'add':'bar'
#     },
#     {
#         'name':'naha',
#         'gender':'female',
#         'age':28,
#         'add':'sonb'
#     }
# ]
# b = list(map(lambda info:(info['name'],info['age']),comapny_info))
# print(b)


# # numbers greater than 5
# a = [2,5,5.6,5.2,9,8,6,7,7.7,7.77,8.23]
# b = list(map(lambda x:x>5,a))
# print(b)





# # # 2. 🔹filter
# # numbers grater than 6
# l = [1,2,3,6,5,7,9,8,8.877,6.6,6.9,10.12,12.5]
# r = list(filter(lambda x:x>6,l))
# print(r)

#  # fetch fruits starting woth 'a'
# fruits = ['apple','banana','mango','graper','papaya','avacado']
# result = list(filter(lambda x:x.startswith('a'),fruits))
# print(result)




# # 2. 🔹Reduce
import functools
a = functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
print(a
)


#sum of all items in a list
b = [2,3,4,5,6]
c = functools.reduce(lambda x,y:x+y,[1,2])
print(c)


# find min
d = functools.reduce(lambda x,y:x if x<y else y ,[2,5,9,7,2,90,76,-1,45])
print(d)


# find max
e = functools.reduce(lambda x,y: x if x>y else y,[3,2,6,7,10,3,19,16,14])
print(e)