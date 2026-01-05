# # 🔹 🔹🔹 Tuples 🔹🔹🔹
# ''' --> A Tuple in python is similat to a list. The difference between the two is that we cannot change the element of a tuple
# once it is assigned whereas we can chanfe the elements of a list.'''

# # 🔹Charactestics
# # --<> Orderd
# # --<> Unchangable
# # --<> Allows duplicate



# #1. 🔹Creating Tuple🔹
# t1 = ()
# print(type(t1))
# print(t1)


# # create a single item tuple
# t2 = (2,) # here we need to use comma , for the single item tuple
# print(t2)

# # homogeneous tuple
# t3 = (1,2,3,4,5)
# print(t3)

# # hetrogeneous tuple
# t4 = (1,2,3,4,True,[1,2,3,4])
# print(t4)

# # 2D tuple
# t5 = (1,2,3,4,(6,7,8))
# print(t5)

# # using type conversion
# t6 = tuple('Hello')
# print(t6)



# # 2.🔹Accessing items🔹
# # 🔹<> By indexing
# a = (1,2,3,4,5)
# print(a)
# print(a[-3])
# print(a[2])

# # 🔹<> By Slicing
# b = (1,2,3,4,5)
# print(b[1:2:2])
# print(b[2:5:2])

# print(a[-2:-3:-1])




# # 3.🔹Editing items🔹
# b = (1,2,3,4,5)
# b[2] = 20
# print(b) # it will not change because tuples are immutable

# # 4.🔹Adding items🔹
# c = (3,4,5,6,743,3,2)
# c.append(222) # it is not possible because it is immutable


# # 5.🔹Deleting Items🔹
# m = (22,3,3,4,455,66,77,88,99)
# del m
# print(m) # it will work on only one case if we delete the whole tuple we cannot delete the item from the tuple


# # 6.🔹Operations & functions on Tuple🔹

# # 🔹+ and *
# t1 = (1,2,3,4,5)
# t2 = (6,7,8,9,10)
# print(t1+t2)
# print(t1*4)
# print(t2*3)


# # 🔹membership
# t1 = (10,20,30,40,50)
# r = 20 in t1 
# s = 34 in t1 
# print(r)
# print(s)


# # 🔹iteration
# t1 = (2,4,6,8,10)
# for i in t1[:3]:
#     print(i)
# print()

# t2 = (3,6,9,12,15)
# for i in t2:
#     print(i)



# # 7.🔹 Tuple Functions🔹
# # 🔹len/sum/max/min/sorted
# t = (3,5,2,6,4,9,7,5,10,33,19,47)
# t1 = len(t)
# t2 = sum(t)
# t3 = max(t)
# t4 = min(t)
# t5 = sorted(t)
# t6 = print(t)
# t7 = print(sorted(t,reverse = True))
# c = (t6,t1,t2,t3,t4,t5,t7)
# for i in c:
#  print(i)


# # 🔹count
# t2 = (4,8,12,16,20)
# a = t2.count(5)
# print(a) # it shows the how many i=times the mentioned items are existing inthe tuple


# # 🔹index
# t4 = (6,5,4,2,4,7,8,9)
# g = t4.index(2)
# print(g) # it shows that at which position the item is existing in a tuple



# # # # 7.🔹 Tuple Unpacking🔹
# # 🔹
# # a,b,c = (1,2,3)
# # print(a,b,c)

# # 🔹Swap value
# a = 5
# b = 9
# a,b = b,a
# print("a is",a ,"and b is",b)

# # 🔹
# a,b,*others = (2,3,4,63,54)
# print(a,b)
# print(others) # it is helpful if we dont give any personal variable to the items, then we can randomly print through this method.


# # # # 7.🔹 Zip Function🔹
# a = (1,2,3,4,5,6,7,8)
# b = (9,8,7,6,5,4,3,2)

# z2 = list(zip(a,b))
# z2.append((5,2))
# z = tuple(zip(a,b))

# print(z2)
# print(z)