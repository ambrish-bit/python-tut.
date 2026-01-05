# # Strings are sequence of characters used to store and manipulate text data.
# ''' in python specifically,strings are a sequence of Unicode characters enclosed within single quotes(' '), 
# double quotes(" "), or triple quotes(''' ''' or """ """).'''

# # <>Creating Strings
# # Accessing Strings
# # Adding Characters to Strings
# # Removing Characters from Strings
# # String Operations
# # String Methods   
# # String functions
# # editing Strings


# # <>Creating Strings
# string1 = 'Hello, World!'  # Using single quotes
# string2 = "Hello, World!"  # Using double quotes
# string3 = '''Hello, World!'''  # Using triple quotes
# string4 = """Hello, World!"""  # Using triple quotes for multi-line strings

# # Accessing Substring from a Strings

# # positive indexing
# str = "Hello, World!"
# print(str[2])

# # negative indexing
# print(str[-4])
# print(len(str))  # length of the string

# # slicing
# s = "Hello World!!"
# print(s[0:5])  # Output: Hello
# print(s[6:])   # Output: World!!
# print(s[:])  # Output: Hello World!!
# print(s[0:8:2])


# # negetive slicing
# print(s[-1:-8:-1])  # Output: !!dlro
# print(s[-6:])  # Output: World!!
# print(s[:-1])  # Output: Hello World!  
# print(s[6:0:-2])  

# print(s[::-1])  # Output: !!dlroW olleH (reverse string)


# # <> Editing and deleting strings
# s = 'Hello, World!'
# s[0] = 'h'  # This will raise an error because strings are immutable


# #  deleting a string
# del s
# print(s)  # This will raise an error because s has been deleted

# s = "Hello, World!"
# del s[-1:-6:2]
# print(s)  # This will raise an error because strings are immutable



# # <>String Operations

# <> Arithmetic Operations
# <> Relational Operations
# <> Logical Operations
# <> Membership Operations
# <> Loops on Strings

# # <> Arithmetic Operations

# print("Delhi" + " " + "Mumbai")  # Concatenation
# print("Delhi"*3)  # Repetition
# print("*"*10)  # Repetition of special character



# # # <> Relational Operations

# print('Delhi' == "Delhi")  # Equality check
# print('Delhi != Delhi')  # Inequality check
# print('Delhi'>'Mumbai')  # Greater than
# print('Delhi'<'Mumbai')  # Less than



# # # <> Logical Operations

# print('Delhi' and 'Mumbai')  # Logical AND
# '''here python checks the first value if it is false 
# it returns that value otherwise it returns the second value eg:- print('' and 'Mumbai') it will return mumbai
# '' but in this case both are true so it returns the second value (And operator me last value print hoga!)'''

# print('Delhi' or 'Mumbai')  
# '''Logical OR ( here python checks the first value if one is true
# it returns that value otherwise it returns the second value) eg:- print('' or 'Mumbai') it will return Mumbai
# but in this case both are true so it returns the first value (Or operator me pehla value print hoga!)'''

# print(not 'Delhi')  # Logical NOT
# ''' here python considers non-empty strings as true so it returns false'''




# # # <> Loops on Strings

# for i in "Hello":
#     print(i)

# for i in 'Mumbai':
#     print('pune')



# # # <> Membership Operations
# print('H' in 'Hello')  # Membership check (True)
# print('h' in 'Hello')  # Membership check (False)




# # <imp> String Functions

# common Functions:

#-> len(): returns the length of the string.
#-> max(): returns the maximum character in the string based on ASCII value.
#-> min(): returns the minimum character in the string based on ASCII value.
#-> sorted(): returns a sorted list of characters in the string.

# a = "Hello, World!"
# print(len(a))       # Output: 13
# print(max(a))      # Output: r
# print(min(a))      # Output:  ' ' (space character)
# print(sorted(a))   # Output: [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
# b = sorted("Hello, World!",reverse=True)   # Output: [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
# print(b)
# print(sorted(a,reverse=True))   # Output: ['r', 'o', 'o', 'l', 'l', 'l', 'e', 'd', 'W', 'H', ',', '!', ' ']
# # # Note: Strings have many built-in methods for various operations like case conversion, searching, replacing, splitting, and joining.


# # # <imp> String Methods
# # common Methods:
# #-> capitalize(): Capitalizes the first character of the string.
# #-> Title(): Capitalizes the first character of each word in the string.
# #-> upper(): Converts all characters in the string to uppercase.
# #-> lower(): Converts all characters in the string to lowercase.
# #-> Swapcase(): Swaps the case of each character in the string.
# #-> find(): Searches for a substring and returns the index of its first occurrence. Returns -1 if not found.
# #-> count(): Counts the occurrences of a substring in the string.
# #-> index(): Searches for a substring and returns the index of its first occurrence. Raises an error if not found.
# #-> endswith(): Checks if the string ends with a specified suffix.
# #-> startswith(): Checks if the string starts with a specified prefix.



# s = "hello world!"
# print(s.capitalize())  # Output: Hello, world!
# print(s.title())       # Output: Hello, World!
# print(s.upper())       # Output: HELLO, WORLD!
# print(s.lower())       # Output: hello, world!
# print(s.swapcase())    # Output: HELLO, WORLD! it canges lower to upper and upper to lower
# #-> find(): Searches for a substring and returns the index of its first occurrence. Returns -1 if not found.

# print(s.find('world'))  # Output: 6 it returns the starting index of the substring
# print(s.find('Python'))  # Output: -1 it returns -1 if substring not found
# #-> count(): Counts the occurrences of a substring in the string.
# print(s.count('l'))  # Output: 3
# print(s.count('z'))  # Output: 0
# print(s.count('!'))
# #-> index(): Searches for a substring and returns the index of its first occurrence. Raises an
# # error if not found.
# print(s.index('world'))  # Output: 6
# # print(s.index('Python'))  # This will raise a ValueError because 'Python' is not found in the string

# print(s.endswith('ld!')) # it checks the string ends with specified suffix
# print(s.startswith('he')) # it checks the string starts with specified prefix



# # # <> format
# # it is used to format the string by replacing the placeholders with the specified values, also order matters in format function.
# name = 'ambrish'
# gender = 'male'
# age = 20
# print('Hii! , my name is {} and I am a {}, I am {} years old'.format(name,gender,age))
# print('Hii! , my name is {1} and I am a {2}, I am {0} years old'.format(age,name,gender))  # order matters in format function



# # isalnum(): checks if all characters in the string are alphanumeric (letters and numbers).
# # isalpha(): checks if all characters in the string are alphabetic (letters only).
# # isdigit(): checks if all characters in the string are digits (numbers only).
# # isidentifier(): checks if the string is a valid identifier (variable name).
# # islower(): checks if all characters in the string are lowercase.

# a = 'Hello1234'
# print(a.isalnum()) # True because it contains only letters and numbers
# print(a.isalpha()) # False because it contains numbers
# print(a.isdigit()) # False because it contains letters
# print(a.isidentifier()) # True because it is a valid identifier
# print(a.islower()) # False because it contains uppercase letters


# # # <> Splitting and Joining Strings
# # # split(): splits the string into a list of substrings based on a specified delimiter (default is whitespace).
# # # join(): joins a list of strings into a single string using a specified delimiter.

# split = 'hi my name is Ambrish'.split()
# print(split)  # Output: ['hi', 'my', 'name', 'is', 'Ambrish'] it breaks the string into list of substrings based on whitespace (word by word)


# split = 'hi my name is Ambrish'.split('i')
# print(split)  # Output: ['hi my', 'name is Ambrish'] it breaks the string into list of substrings based on 'i' character


# #  join
# join = ' '.join(['hi', 'my', 'name', 'is', 'Ambrish'])
# print(join)  # Output: hi-my-name-is-Ambrish it joins the list of strings into a single string using '-' as delimiter



# # # <> Replace
# # # replace(): replaces occurrences of a specified substring with another substring.
# s = "Hii, my name is Ambrish. and I am a developer. Ambrish is my name."
# s1 = s.replace('Ambrish', 'Raj')
# print(s1)


# z = "Hii The moon looks so pretty tonight and moon is very far from us"
# z1 = z.replace('moon', 'Wo') # # it replaces all occurrences of 'moon' with 'Wo'
# print(z1)


y = "Hiion myyy     name      is   Ambrish"
y1 = ' '.join(y.split())  # it removes extra spaces between words
print(y1)


y = "Hiion myyy     name      is   Ambrish"
y.strip()  # it removes leading and trailing spaces
print(y) == y.lstrip()  # it removes leading spaces
print(y1) == y.rstrip()  # it removes trailing spaces
print(y1)