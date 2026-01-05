# ### 🔹🔹🔹 Dictionary 🔹🔹🔹###
# '''Dictionary in python is a collection of keys values, used to store data values lie a map,
# which, unlike other data types which hold onlu a single value as an element . A dictionary in Python is a data type used to store data in pairs — called key : value pairs.

# In easy words:

# A dictionary is like a real-life dictionary:

# You look up a word (key)

# You get its meaning (value)'''

# # # in some languages it is known as map or assosiative arrays.
# # dict = {'name':'nitish','age':33,'gender':'male'}
# # print(dict)

# ## <🔹>  Characterstics --
# # --> mutable
# # --> indexing has no meaning
# # --> keya can't be duplicated
# # --> keys can't be mutable items


# ## <🔹> Create Dictionary
# # --> Empty dictionary
# d = {}
# print(d)

# # --> 2D dictionary
# d1 = {'name':'Ambrish','age' : 20,'gender' : 'male'}
# print(d1)

# # --> with mixed keys
# d2 = {(1,2,3):1,'hello':'world!',}
# print(d2)


# # --> 2D dictionary
# s = {
#     'name' : 'Ambrish',
#     'college': 'Parul',
#     'sem' : 4,
#     'subjects' :{
#         'python':88,
#         'java':78,
#         'cpp':81,
#         'c' : 90
#     }

# }
# print(s)


# # --> using sequence and dict function
# d4 = dict([(9,10),(11,12),(13,14)])
# print(d4)

# # --> using sequence and dict function
# d5 = dict([('name','Ambrish'),('college','parul'),('subject','dsa')])
# print(d5)


# # --> duplicate keys
# d6 = {'name':'Amb','name':'Raj'}
# print(d6)


# # --> mutable items as keys
# d7 = {'name':'Ambrishh',(1,2,3):2}
# print(d7)




# ## <🔹> Accessing Items
# my_dict = {'name':'Ambb','age':20}
# a = my_dict['name']
# b = my_dict['age']  # we can access the items only through the key.
# print(a)
# print(b)



# ## <🔹> Adding key value pairs
# d7['gender'] = 'male'
# print(d7)
# d7['weight'] = 60
# print(d7)



## <🔹> Remove Key Value Pairs
# d8 = {'name': 'Ambrishh', (1, 2, 3): 2, 'gender': 'male', 'weight': 60}
## --> pop
# d8.pop('name')
# print(d8)

# # --> popitem
# d8.popitem()
# d8.popitem()
# print(d8)

# # --> del
# del d8['name']
# print(d8)
# del d8['gender']
# print(d8)


# # --> clear
# d8.clear()
# print(d8)


# # <🔹> Adding key-Value Pairs in 2D
# st = {
#     'name':'Amb',
#     'clg':'Parul',
#     'age':20,
#    'subject':{'dsa':79,'maths':88,'python':89,'java':90},
#     }
# # print(st)
# # st['subject']['dsa'] = 82  # it is usable for the change the value of any key, it shows by square bracket, how many Diamension are there that much time brackets are required.
# # print(st)



# ## <🔹> Remove key-Value Pairs in 2D
# del st['subject']['maths']
# print(st)



# ## <🔹> Editing key-Value Pairs in 2D
# st['subject']['python'] = 93
# print(st)



# ## <🔹> Dictionary Operation
s = {
    'name':'Amb',
    'clg':'Parul',
    'age':20,
   'subject':{'dsa':79,'maths':88,'python':89,'java':90},
    }
# # --> Membership
# print(s)
# cc = 'subject' in s
# print(cc)
# # --> Iteration




# ## <🔹> Dictionary Functions
#--> len/sorted/min/max
## len
# l = len(s)
# print(l)
# print(s)

# #sorted
# print(sorted(s))

# #min
# print(min(s))

# #max
# print(max(s))


# ## items/keys/values
# #items
# print(s.items())  # it prints the all value 

# #keys
# print(s.keys()) #it prints the all key 

# #values
# print(s.values())  # it prints all the value of the keys.


# ## Update
# s1 = {1:2,2:3,3:4,4:5}  # we can edit the given dictionary by the help of another dictionary.
# S2 = {2:5,4:9,1:5}  # this method edit the value in the dictionary.
# s1.update(S2)
# print(s1)





# # ## <🔹> Dictionary Comprehension
# #--> print 1st 10 numbers and their squares
# c = {i:i**2 for i in range(1,11)}
# print(c)


#--> Using existing dict
# distances = {'Delhi':1200,'GKP':1400,'Hydrabad':800,'banglore':900}
# d = {key:value*0.62 for (key,value) in distances.items()}
# print(d)

# ## -> Using Zip
# days = ["Sunday","Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday']
# temp_c = [30.5,33,35,26,28,29,31]
# m = {i:j for (i,j) in zip(days,temp_c)}
# print(m)

# subject = ['Hindi','English','Math','Physics','Science','Chemistry']
# marks = [77,80,78.7,69,82,86]

# ma = {i:j for (i,j) in zip(subject,marks)}
# print(ma)


# ## using if condition
# products = {'phone':13,'batteries':27,'phone case':40,'charger':32,'user':22}
# b = {key:value for (key,value) in products.items() if value>=15}
# print(b)


# ## Nested comperhension
# print table of number from 2 to 4
t = {j:{i:j*i for i in range  (1,11)} for j in range (2,5)}
print(t)