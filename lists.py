# ### <> LIST ###
# '''A Python list is an ordered, changable(mutable) collection of items
# defined by enclosing elemments in square brackets ([]).
# Lists are highly flecible and can store items of different data types, including integers,
# strings, and even other lists.'''

# # # <> What are Lists?
# '''list is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic
# arrays which means you can add more items on the fly.'''


# # # <> Lists Vs Arrays
# '''<> Fixed Vs Dynamic Size:
# <> Convinience (Homogeneous(same type data)) -> Hetrogeneous (multiple type data str,char,int float, list etc,,.) 
# <> Speed of Execution: Arrays are generally faster than lists for numerical operations due to their fixed size and homogeneous data types.
# <> Memory (Lists tae more space then arrays because of their dynamic nature and ability to store different data types.)'''


# # # <> Characteristics of Lists:
# '''<> Ordered: The items in a list have a defined order, and that order will not change unless you explicitly modify the list.
# <> Changeable (Mutable): You can change, add, and remove items in a list after it has been created.
# <> Allow Duplicates: Since lists are indexed, they can have items with the same value.
# <> Heterogeneous: Lists can contain items of different data types.
# <> Dynamic Size: Lists can grow and shrink in size as needed.
# <> Indexed(items can be accessed): Each item in a list has an index, which is its position in the list. The first item has an index of 0, the second item has an index of 1, and so on.
# <> Nested: Lists can contain other lists as items, allowing for the creation of complex data structures.
# <> Iterable: Lists can be looped through using loops like for and while.
# <> Built-in Functions and Methods: Python provides a variety of built-in functions and methods to manipulate lists, such as append(), remove(), sort(), and more.
# <> can contain any kind of object in python.'''


# # # <> How to create list
# # -> Empty List
# empty_list = []
# print('Empty List', empty_list)

# # -> 1D
# one_d_list = [1,2,3,4,5]  # Homogeneous list
# print('1D List', one_d_list)

# # -> 2D
# two_d_list = [[1,2,3],[4,5,6,["j","k",9,True]]] # hetrogeneous list
# print('2D List',two_d_list)

# #  -> 3D
# three_d_lists = [11,12,[13,14,15,15.5,[16,17,18]]] # it means there will list inside the list inside the list.
# print('3D List', three_d_lists)

# # -> using Type Conversion
# print(list('Hello'))






# # # <> Access items from a list
# # -> Positive Indexing
# A = [1,2,3,4,5,6]
# print(A[3])
# B = [[[1,2],[3,4],[5,6]]]
# print(B[0][2][1])
# print(B[0][0][1])
# # -> Negative Indexing
# print(A[-4])

# # -> Slicing
# r = ['a','m','b','r','i','s','h']
# print(r[2:5])
# print(r[ : ])
# print(r[ : 2])
# print(r[3: ])
# print(r[-5 : -2])
# print(r[0::3])
# print(r[::-1])


# # # <> Adding items to a list
# # # -> Using append()
# a = [1,2,3,4,5,6,7]
# a.append(True)
# a.append('k')
# print(a)

# l = [1,2,3,4,5]
# l.append('delhi')
# print(l)


# # extend() it is use for adding many items
# o = [21,20,19]
# o.extend([11,12,13,14])
# print(o)

# c = ['x','y','z']
# p = ['r', 's','o','t',c]
# p.extend([19,20,30])
# print(p)

# l = [1,2,3,4,5]
# l.extend('delhi')
# print(l)


# # insert() it is use for adding item at specific index
# m = [1,2,3,4,5,6]
# m.insert(3,100)
# print(m)




# # ## <> Editing items in a list
# a = [1,2,3,4,5,6,7,8,9,0]
# # editing with indexing
# a[4] = 'k'
# # a[2:-1] = 300,100
# # editing with slicing
# a[2:5] = [100,200,300]
# print(a)




# # # <> Deleting items from a list
# # using del keyword with slicing
# a = [1,23,4,5,6,7,8,9]
# del a[2:5]
# print(a)
# del a
# print(a)

# b = [1,23,4,5,6,7,8,9]
# # using del keyword with indexing
# del b[-3]
# print(b)

# # using remove() method
# # it will delete the value which we mentioned in the method
# u = [1,2,3,4,5,6,7,8,9]
# u.remove(4)
# print(u)


# # using pop() method
# e = [1,2,3,4,5,6,7]
# # it will delete the item using index we mentioned
# e.pop(3)
# print(e)


# r = [9,8,7,6,5,4,3,2,1]
# # it will delete the last item of list if we not mentioned the index which we want to delete.
# r.pop() # it will delete from -1 index
# print(r)

# # using clear() method
# uv = [5,6,7,8,9]
# uv.clear()
# print(uv)






# # # <> Operations on Lists

# # --> Arithmetic operations
# a1 = [1,2,3,4]
# a2 = [5,6,7,8]
# print('concatination:', a1+a2)  # concatination
# print('repitatation', a1*4)   # repitatation, means it will repeat the list 4 time and merge in it.


# # ->> Membership Operators
# u1 = [10,20,30,40,50,60,70]
# u2 = [33,44,55,66,77]
# print(7 in u1)
# print(66 in u2)
# print(100 not in u2)


# # ->>> Loop
# cc = ['a','b','c','d','e']
# for i in cc:
#     print(i)

# cc = ['a','b','c','d','e',[1,2,3,4,5,6]]
# for i in cc:
#     print(i)

# cc = [['a','b'],['c','d','e']],[[1,2,3,4,5,6],[7,8,9,10,11]]
# for i in cc:
#     print(i)


# # # <> Functions on lists
# # --> len/min/max/sorted
# aa = [1,2,3,4,5,'amb']
# print(len(aa))

# bb = [10,20,30,40,50]
# print(min(bb)) # min will work only if we have te homogeneous data

# kk = [10,20,30,40]
# print(max(kk)) # max will also work on the homogeneous data only

# oo = [3,1,6,4,0,6,8,55,3,99,2]
# print(sorted(oo,reverse=True))


# # --> count() it will count how many times the item is present in the list
# l = (1,1,2,34,5,6,8,9,6,4,3,4,56,7)
# print(l.count(1))


# # --> INDEX it will give the index of the item we mentioned in the method
# p = [1,2,3,4,5,6,77,83,21,3,1,5]
# print(p.index(1))


# # --> reverse() it will reverse the list
# q = [8,7,6,5,4,3,2,1]
# q.reverse()  # it is use for permanent change in the list
# print(q) 

# # --> sort() it will sort the list in ascending order by default
# l = [5,3,8,1,2,7,4,6]   
# l.sort()  # it is use for permanent change in the list where sorted is not for permanent change
# print(l)

# # --> copy() it will create the copy of the list
# l = [1,2,3,4,5]
# print(l)
# print(id(l))
# m = l.copy()
# print(m)
# print(id(m))





# # ### 🔹 List Comprehensions  ###
# # '''List comprehension is a short and simple way to create a list in 
# # Python using one line of code instead of writing a loop.'''
# # # 🔹 General format
# # # [expression for item in collection]

# # 1️⃣ Normal way (using loop)
# # # 🔹add 1 to5  numbers in a list
# # # code using loop
# # a = []
# # for i in range(1,6):
# #   a.append(i)
# # print(a)

# # 3️⃣ Example: Create a list of numbers
# # # code using comprehension
# # b = [i for i in range(1,6)]
# # print(b)


# # 🔹scalar multiplication on a vector
# a = [3,4,6,8]
# b = -5
# c = []
# for i in a:
#     c.append(i*b)
# print(c)

# # 🔹multiplication on a vector using comprehension
# a = [3,4,6,8]
# b = -5
# c = [b*i for i in a]
# print(c)


# # 2️⃣ List comprehension way
# # 🔹Add square 
# l = [1,2,3,4,5]
# m = []
# for i in l:
#  m.append(i**2)
# print(m)

# # 🔹Add square using comprehension
# l = [1,2,3,4,5]
# j = [i**2 for i in l]
# print(j)


# # 4️⃣ With condition (if)
# # 🔹print all the numbers which are divisible by 5 in the range of 1 to 50
# '''it will use for coditions like (if)'''
# a = []
# for i in range(1,51):
#    if i%5 == 0:
#       a.append(i)
# print(a)

# # 🔹print even number from 1 to 50
# a = []
# for i in range(1,51):
#    if i%5 == 0:
#       a.append(i)
# print(a)
   
# # 🔹print even number from 1 to 50 using comprehension
# '''it will work in sort line'''
# a = [i for i in range(1,51) if i%2==0]
# print(a)

# # 🔹Find languages which start with letter p
# languages = ['c','cpp','python','java','php','javascript','c#']
# for i in languages:
#   if i.startswith('p'):
#      print(i)

# # 🔹Find languages which start with letter p using comprehension
# languages = ['c','cpp','python','java','php','javascript','c#']
# a = [language for language in languages if language.startswith('c')]
# print(a)


# # 🔹<> Nested if with list comprehension
# # add new list from my_fruits and items if the fruits exists in basket and also starts with 'a'

# basket = ['apple','guava','cherry','bnana',]
# my_fruits = ['apple','kiwi','grapes','banana']
# fruit = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]

# print(fruit)


#  # #🔹<> Print a (3,3) matrix using list comprehension -> Nested List comprehension
# matrix = [[i+j for i in range(1,4)] for j in range(1,4)]
# print(matrix)

# # #🔹<> Cartesian product -> List comprehension  on 2 lost together
# L1 = [1,2,3,4,5]
# L2 = [6,7,8,9,10]
# matrix2 = [[i*j for i in L1] for j in L2]
# print(matrix2)



# ### 🔹🔹🔹2 ways to traverse(run a list) a list 🔹🔹🔹###
# # 1. 🔹 Itemwise
# a = [1,2,3,4,5,6]
# for i in a:
#     print(i)
#     print()

# # 2. 🔹 Indexwide
# b = [1,2,3,4,5,6]
# for i in range(0,len(b)):
#     print(b[i])




### 🔹🔹🔹Zip Function🔹🔹🔹###
'''The zip Fuunction is used to combine two or more lists (or other sequences)
element-by-element into pairs( or tuples).'''
a = [-11,20,-42,17,-26,45,-50,23,-74,55]
b = [20,-15,47,-12,35,-36,51,-21,74,-49]
list(zip(a,b))
bb = [i+j for i,j in zip(a,b)]
print(bb)