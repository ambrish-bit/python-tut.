# # if-else is used fofr to make decision in a program
# # it checks condition
# # if condition:
#  #code runs if decision is true
# #  else condition
#  #code runs when condition is false


# # login progra and identation
# # email - abc123@gamil.com
# # password - 1234

# email = input('ENTER YOUR EMAIL ')
# password = input('ENTER YOUR PASSWORD ')

# if email == 'abc123@gmail.com' and password == '1234':
#     print('Welcome')
# elif email == 'abc123@gmail.com' and password != '1234':
#     print('Incorrect Password')
#     password = input('Enter password again ')
#     if password == '1234':
#         print('Welcome Finally')
#     else:
#         print('beta tumse na ho payega!')

# else: 
#     print('Pass or Email is incorrect')



# # <> python has indentation , so we have to code in correct form to make the code beautiful




# # problem- find the min of 3 number

# a = int(input('first num '))
# b = int(input('second num '))
# c = int(input('third num '))

# if a<b and a<c:
#     print('smallest is ',a)
# elif b<c and b<a:
#     print('smallest ',b)
# else:
#     print('smallest is ',c)


# problem - menu driven caLCULATOR

fnum = int(input('Enter the 1st num '))
snum = int(input('Enter the 2nd num '))

op = input('Enter the operation ')
if op == '+':
 print(fnum + snum)
elif op == '-':
 print(fnum - snum)
elif op == '*':
 print(fnum * snum)
elif op == '/':
 print(fnum / snum)
else:
   print('not match!')

