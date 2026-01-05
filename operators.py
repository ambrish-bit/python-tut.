# Operators are special symbol that perform operations on values or variable
# They are used to calculate, compare, and manipulate data.


# <>Operators in pyhton

# ->Arithmetic Operators
# ->Relational Operators
# ->Logical Operators
# ->Bitwise Operators
# ->Assignment Operators
# ->Membership Operators

# 1. Arithmetic Operators
print(5+6)

print(4-3)

print(2*4)

print(5/6)

# it converts the decimal value into integer value and give the int output
print(5//2) 

print(5%2)

# power of (use for find power value)
print(5**2)



# 2. Relational Operators
print(4>5)

print(4<5)

print(4>=4)

print(4==4)

print(4<=4)

print(4!=4)



# 3. Logical Operators
print(1 and 0)

print(1 or 0)

print(not 1)



# 4. Bitwise Operators
# Bitwise and oper
# it shows trhe binare patern result of both num(if both value 1 then it gives 1 otherwise it gives 0)
print(2 & 3)

# bitwise OR oper
# it gives 1 if any one value is 1 from both binary number has 
print(2 | 3)

# Bitwise xor
# it gives 1 if both value saperate and gives 0 if both vale are same
print(2 ^ 3)

# left shift
print(4>> 3)



# 5. Assignment Operator '='
a=2

# a = a%2
a%=2
# a+=2
# a-=2
# a*=2
print(a)


# 5.Membership Operator

# in / not in
# it shows the value is existing or not in the data base
print('D' in 'Delhi')
print('D'  not in 'Delhi')

print(1 in [2,3,4,5,6,7,89])



# Program - Find the sum of a 3 digit nnumber entered by the user
number = int(input('Enter a 3 digit number '))

# 345%10
a = number%10

number = number//10

# 34%10
b = number%10


number=number//10
# 3%10
c = number%10

print(a+b+c)