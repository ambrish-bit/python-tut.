# whatever raw we store in any variable is said to be literal
# it means when we define anything by any raw then it could said to literal.
# eg:- a = 2 (in that a is variable, '=' is the operator and 2 is the literal)

# <> there's many way to set any literal
#  1.Integer Literal
a = 0b1010 # Binary literal
b = 100    # Decimal literal
c = 0o310  # Octal literal
d = 0x12c  # Hexadecimal literal

# 2. Float Literal
float_1 = 10.5
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-2

#3. Complex Literal
x = 3.14j
print(x)
print(x.real,x.imag)
print(x.real)
print(x.imag)

#4. Strings Literal
string = 'This is a string'
strings = "This is String"
char = "C"
multiline_str = ''' hii everyone my name is Ambrish gupta and i am learning python from the scratch'''
unicode = u"\U0001f600\U0001F606\U0001f923"  #this is for unicode thigs like smily/emojies
raw_str = r"raw \n String" # this is for line change , tab... etc.

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# 5. Boolean Literal
a = True + 5.2 # here's the value of tru is 1 and value of false is zro
b = False + 3 * False   # we can perform the operations using that in declaration

print('a',a)
print('b',b)


''' none is use for variable declaration , if we want to store any value and use in fututre then we should have to use the none keyword , by 
using this keyword we can easily save that variable for the future usese'''

# eg:-
k = None
a = 1
b = 2
print ('program exec')