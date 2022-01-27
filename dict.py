



# thisdict={
#     "name":"Nitesh",
#     "Year_of":2001,
#     "Education":"B.tech"
# }
# thisdict["Year_of birth"]=2002
# print(thisdict["Education"])
# print(thisdict.get("name"))
# print(thisdict["Year_of"])


# thisdict["Branch"]="CSE"
# # thisdict.pop("name")
# # thisdict.popitem()
# thisdict["surname"]="Reddy"
# # del thisdict["surname"]
# # thisdict.clear()
# for x in thisdict:
#     print(x,thisdict[x])

# for x in thisdict.values():
#     print(x)
# for x in thisdict.keys():
#      print(x)
    
# for x,y in thisdict.items():
#     print(x,y)




#COPY A DICTIONARY
# dict1={ "name":"Nitesh","age":19}
# dict2={"firstname":"kumar",
# "agef":19}
# mydict=dict1.copy()
# for x ,y in mydict.items():
#     print(x,y)
# yourdict=dict2.copy()
# for x,y in yourdict.items():
#     print(x,y)



#nested dictionaries
myfamily={
 "child1":{
     "name":"Nitesh",
     "age":19
 },
 "child2":{
     "name":"kumar",
     "age":19
 },
 "chid3":
 {
     "name":"Reddy",
     "age":18
 }
}

for x in myfamily.keys():
    for a,b in x.items():
        print(a,b) 