##🔹 Sets🔹 ##
'''A set is an unordered collection of items. Every set element is unique(no duplicates) and must be immutable (cannot be change).
Howeever, a set itself is mutable. We add or remove items from it.'''
'''Sets can also be used to perform mathematical set operaations like union, intesection, symmetric difference,etc.'''
# 🔹<> Characterstics:
# 🔹 Unorderd
# 🔹Mutable
# 🔹No duplicates
# 🔹can't contain mutable data types


# ##🔹Creating Sets
# # <>  empty
# a = set()
# print(a)
# print(type(a))


# # <> 1D and 2D
# s1 = {1,2,3}
# print(s1)
# print(type(s1))

# # s2 = {1,2,3,{4,5}}
# # print(s2)
# # print(type(s2))  # you cannot have a mutable value inside the set , that's why it give the typeerror.


# # <> homo and hetro
# s3 = {1,2,3,4,5}
# print(s3)  # Homogenious

# s4 = {1,True,0.1,1,'hello',(1,2,3)}
# print(s4) # cannot contain duplicate value


# # <> using type conversion
# s5 = set([1,2,3,4])
# print(s5)


# # <> duplicates not allowed
# s6 = {1,1,2,2,3,3,54,6,5,3,5,7,9}
# print(s6)


# # # <> sets can't have mutable items
# # s7 = {1,2,3,4,[1,2,34]}
# # print(s7) # it cannot contain the mutable value into the set, and it will give the error unhashabble type: llist 

# s1 = {1,2,3}
# s2 = {3,2,1}
# print(s1 == s2)



##🔹Accessing items
'''we cannot access the items of sets through the indexing, slicing or even in any other ways. '''


##🔹Editing items
'''int the term of the set editing is also unable to work, means we cannot edit the items of set through any mathods.'''


# ##🔹Adding items
# S = {1,2,3,4,5}
# # add
# S.add(7) # it will add only one value at a time
# print(S)

# #update
# S.update([12,13,14,15]) # it will add more then one items at a time.
# print(S)


##🔹Deleting items
# s  = {1,2,3,4,5,6}
# print(s)
# del s
# del s[2]  # we can delete the whole set but we cannot delete the single items throuth the indexing or slicing in the the set.
# print(s)

# #discard
# s.discard(5)
# print(s) # we can remove any one item from the set through the discard method, it will not the give the error if the item is not exist which we mentioned for the remove..

# #remove
# s.remove(3)
# print(s) # it can also del single value fromt the list but it will give the error if the value is not existing in the set which we mentioned for the deletion.

# #pop
# s.pop()
# print(s) # it will delete any randim value from the list.

# #clear
# s.clear() # it will clear all the set.
# print(s)



# ##🔹Set Operations
# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# # <> Union (|)
# a = s1|s2 # it will give the value from set s1 and s2 only one time even if value are repeating(common in both set).
# print(a)

# # <> Intersection(&)
# b = s1&s2 # it will give only common value from the sets s1 and s2.
# print(b)

# # <> Difference(-)
# c = s1-s2 # it returns the value which are not present in second one which is use for comparing.
# d = s2-s1
# print(c)
# print(d)

# # <> Symmetric Difference(^)
# e = s1^s2 # it will not return the common values, except of thet it return all the value for one time.
# print(e)


# # <> Membership Test
# f = 1 in s1
# g = 2 not in s2
# print(f)
# print(g)


# # <> Iteration
# for i in s1:
#     print(i)




# ##🔹Set Functions
# # len/sum/min/max/sorted
# # --> len
# s1 = {2,3,4,1,6,9,11,10}
# s2 = {10,12,10,15,2,5,8,20}
# a = len(s1)
# print('len', '=',a)

# # --> sum
# b = sum(s1)
# print('sum', '=',b)

# # --> min
# c = min(s1)
# d = min(s2)
# e = min(s1,s2)
# print('min', '=',c)
# print('min', '=',d)
# print('min', '=',e)

# # --> max
# f = max(s1)
# g = max(s2)
# h = max(s1,s2)
# print('max', '=',f)
# print('max', '=',g)
# print('max', '=',h)

# # --> sorted
# i = sorted(s1)
# j = sorted(s2)
# k = sorted(s2,reverse=True)
# print(i)
# print(j)
# print(k)



# <> union/update
# s1 = {2,4,6,8,10,12}
# s2 = {10,12,14,16,18}

# # --> union
# a = s1.union(s2)
# print(a)

# # -->update
# s1.update(s2)
# print(s1)
# print(s2)

# # <> intersection/intersection_update
# # --> intersection
# s1.intersection(s2)
# # print(s1)

# # --> intersection_update
# s1.intersection_update(s2) # it canges all the value of set 1 by the element of s2, and the set s2 remain the same.
# print(s1)
# print(s2) 



# # <> difference/difference_update
# s1 = {1,2,3,4,5,6,7}
# s2 = {6,7,8,9,10,11}
# # --> difference
# s1.difference(s2)
# # --> difference_update
# s1.difference_update(s2)
# print(s1)
# print(s2)



# # <> symmetric_difference/symmetric_difference_update
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)


# # <> isdisjoint/issubset/issuperset
# s1 = {1,2,3,4,5,6,7,8,9}
# s2 = {4,5,6,7,8}
# a = s1.isdisjoint(s2)
# b = s1.issubset(s2)
# d = s2.issubset(s1)
# c = s1.issuperset(s2)
# print(a)
# print(b)
# print(c)
# print(d)


# # <> copy
# s1 = {1,2,3,4}
# s2 = (2,3,4,5)
# s2 = s1.copy()
# print(s2)




# ##🔹Frozen Set🔹##
# '''Frozen set is hust an immutable version of a python set object.'''

# ##🔹Create Frozenset
# fs = frozenset([1,2,3])
# print(fs)


# ##🔹what works and what does not
'''# union/intersection/isset/issubset/issuperst/isdisjoin and likw those function will perform 
 because it does affect the real set , but like pop/remove/delete/discard/add those type of operation will not work on frozenset.'''

# # -> all read funtions will work

# # -> all write functions will not work


# ##🔹2D frozenset
# fs = frozenset([1,2,frozenset([4,5])])
# print(fs)


# ##🔹Set Comprehension
# #example
# a = {i for i in range(1,11)}
# b = {i for i in range (11,21) if i%2 == 0}
# c = { i for i in range (1,21) if i>=5}
# d = {i**2 for i in range (1,11)}
# print(a)
# print(b)
# print(c)
# print(d)
