#PART 1
# variables in python
# x=89



#PART 2
# y="Nitesh"
# z=90.56
# print(x)
# print(y)
# print(x+z)
# x=str(7)


#PART3
# y="Nitesh"
# print(x)
# print(type(x))
# print(type(y))
# r="Jhon"
# R='jhon'
# # both are same 
# # this will create two varibles
# a=4
# A="KUmar"
# # variables are case sensitive
# print(a)
# print(A)
# Different types of notation for variables
# myVariables="Reddy"  # camel case
# myVariables="Reddy"  # Pascal case

#PART4
# my_variable_name="Reddy" #"Snake case"
# Assiging a value to multiple values
# x,y,z="Nitesh","kumar","reddy"
# print(x)
# print(y)
# print(z)
# print(x+''+y+''+z)


#PART5
# global varibal
# If you create same varibale inside the function and globally it will
#work according to the scope
# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
# myfunc()
# print("Python is " + x)



#PART5
#if you want to create global function inside function
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)  # out put is Python is fantastic



#PART6
# if you want to change global varible inside a function,refer to the 
# variable using global keyword

# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)


#PYTHON NUMBERS

# x=187436520847876
# y=34.89
# z=1j
# print(x)
# print(type(x))
# print(type(y))
# print(type(z))


# Type Coneverison

# x=1
# y=2.8
# z=1j+5
# a=float(x)
# b=int(y)
# c=complex(x)   #You cannot convert complex numbers into another number type.
# print(a)
# print(b)
# print(c)
# print(z)
# print(type(a))
# print(type(b))
# print(type(c))

#RANDOM NUMBER
#puthon doesnot have a random() function to make a random num
#ber but python has buit in moduke called random that cane be
#used to amkle random numbers:

# import random
# print(random.randrange(1,10))


#Multline string
# a=""" iudfhgerwhuoigerhogvirg gyurgyur
# dshegigfreyufgeuhfehgfgr3yfgiryfghuergfiyewgfh
# idfugyukerhyurg yurgf"""
# print(a)



# x="hello"

# print(x)
# print(len(x))
# y="Hey I am Nitesh Kumar Reddy"
# print("am"in y)  # it return true and false
# if "Nitesh" in y:
#     print("Yes")
#     print("work"not in y)

# #slicing python
# b="hello world"
# print(b[2:5])
# print(b[3:8])
# print(b[:5]) #slice from start #hello
# print(b[2:]) #slic to the end  llo world

# #Modify string
# a="  hello world"
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("h","N"))
# print(a.split("o"))

# #string Concatination
# a="Hello"
# b="World"
# c=a+b
# print(c)

# #string fromating
# age=19
# info="Hey my age is {} "
# print(info.format(age))

# day=2
# month=7
# year=2002
# information="MY date of birth is {0} {1} {2}"
# print(information.format(day ,month,year))

#string emthods

# a="hello WorlD"
# print(a.capitalize()) #Converts the first character to upper case
# print(a.casefold()) # converts whole string to lower case
# print(a.center())

#PYTHON BOOLEANS
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a=78
# b=76
# if b>a:
#     print("b is greter then a")
# else:
#         print("a is greter then b")
# print(bool("Hello"))
# print(bool(15))


#python OPERrator
# Arithmetic operators

# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


#list
# names=["kumar","reddy","shyam","ravi"]
# print(names)
# print(type(names))
# # we can use list construtor when we are using lists
# products=list(("apple",45,90.8,True))
# print(products)

#list
# thislist=["mumbai","delhi","america"]
# print(thislist[-1]) #neagtive indexing means strat from last
# fruits=["apple",78,True,False,"mango","america","amazon","micorsoft"]
# print(fruits[2:5])  # range of elements of the list
# #search will strat from index 2 but excluding index
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# if "cherry" in thislist:
#     print("Yes present in the thislist")
# else:
#     print("No not present in the thislist")


#Change list items
# thislist=list(("apples","mango","orange","pinapple","mango"))
# thislist[2]="straberry"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# thislist.insert(2,"Nitesh")
# print(thislist)

# 

# names=list(("NItesh","kumar","reddy","mumbai","delhi"))
# names.append("bangaluru")
# names.append("Hyderabad")
# names.insert(3,"Chennai")
# print(names)
# names.extend(places)
# print(names)


#Remove specified elements
# thislist=["apple","banana","cherry"]
# thislist.remove("apple")
# print(thislist) # it takes the string which is need to be removed
# thislist.pop(1) # it takes the index which is going to remove
# thislist.extend(places)
# print(thislist)
# thislist.pop()# if you donot mention any index it will remove the lat element
# print(thislist)
# del thislist[2]
# print(thislist)
# thislist.clear()
# print(bool(thislist))


#loop through a list
# thislist =["apple","banana","cherry"]
# for x in thislist:
#     print(x)
# for i in range(len(thislist)):
#     print(thislist[i])
# while i< len(thislist):
#  print(thislist[i])
#  i=i+1

#list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# for i in range(len(newlist)):
#     print(newlist[i])
# names=["kumar","shyam","radhe","puspha"]
# new=[x for x in names]
# # list comprehension
# [print(x ) for x in new]
# new = [x.upper() for x in names]
# [print(x) for x in new]
# new=["hello" for x in names]
# [print(x) for x in new]


#sort a list
# names=list(("apple","kumar","timer","shyam","anirudh"))
# names.sort()
# [print(x ) for x in names]
# numbers=[100,89,687,34,777,23]
# numbers.sort(reverse=True)
# [print(x) for x in numbers]
# numbers.reverse()
# [print(x) for x in numbers]


#Copy List
# thislist=["apple","mango","strabeerry"]
# # mylist=thislist.copy() # copy with copy method
# mylist=list(thislist)
# print(mylist)



#join list
# list1=["apple",45,90,True]
# list2=["a","b","bahubali"]
# list3=list1+list2
# print(list3)
# for x in list2:
#     list1.append(x)
# print(list1)
# print(list1.count("apple"))

#Tuple
# thistuple=("apple","banana","cherry")
# print(thistuple)
#Tuple items are ordered ,unchangeable, and allow duplicate values
# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
# thistuple = ("apple",)
# print(type(thistuple))
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
# tuple1=("apple","mango","ccherry")
# tuple2=(12,45,78,90)
# tuple3=(True,False,False)
# print(tuple1)
# print(tuple2)
# print(tuple3)
# tuple4=("Nitesh",11,8,11,2001,"CSE")
# print(tuple4)
# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))


#condiation statement
# a=89
# b=90
# if b>a:
#     print("b is greter then a")
# else:
#     print("a is greter then b")
# a=89
# b=90
# c=34
# if a>b and b>c:
#     print("Both conditiona re true")
# else :
#     print("Not true")
# if a>b or b>c:
#     print("One of the  conditiona is true")
# else :
#     print("Not true")


#loops
#while loop

#continue
# i=1
# while i<7:
#  print(i)
#  if i==3:
#      break
#  i+=1
# i=1
# while i<7:
#  i+=1
#  print(i)
#  if i==3:
#    continue
 

#for loops
# fruits = ["apple", "banana", "cherry"]
# # for x in fruits:
# #   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)
# for x in range(2, 30, 3):
#   print(x)
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

#function
def my_function():
    print("hello to python")
my_function()
def add(a,b):
    c=a+b
    print("value is"+c)
# add("Nitesh","kumar")
add("america","london")
