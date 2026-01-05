# # <> Input 
# input()
# input('Write your name:- ')


# take input from the user and store them in a variable
fnum = input('Enter first number :- ')
snum = input('Enter second number :- ')
print(fnum,snum)
# add the 2 variables
result = int(fnum)+int(snum)
# print the result
print(result)


# <> type conversion (implicit to explicit)
# it is a method to cange one data type to another 


# #  <> implicit type conversion
# # it is done by the interpreture , it means programmers doesn't need to change
# # eg:- here we are using implicit type conversion in following line code
# print(5+5.6) 

# <> Explicit type conversion
# when we convert one data type into another data type manually then it is said to be explicit conversion
# eg:- 

# # a = '5'

# # int(a)
# # print(a)
# # print(type(int(a)))

# b = 4.5
# print(int(b))
# print(type(int(b)))

# it will nort work in every situation , like if we want to chage any complex numer into int then it will give the error

# c = 4
# print(float(c))
print(type(fnum))