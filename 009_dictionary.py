# dictionary data type

# import pprint
from typing import Union

# names : dict[str,str] = {"fname":"Rao Ali Murad",
#                         "education":"learing coding",
#                         "city":"karachi"}
# print(names)
# pprint.pprint(names)
# print(names["fname"])

# for key,value in names.items():
#     print(f" {key}: {value}")


# another example of dictionary

key =  Union[str,int] # create custom data type
# key = int|str         another method to create data type
values = Union[str,bool,int ,list]


names : dict[key,values] = {"fname":"Rao Ali Murad",
                        "education":"learing coding",
                        "city":"karachi",
                        0:"pakistan",
                        "hobbies":["cricket","football","hockey"]}

print(names[0])               # 0 is not a index its a key
print(names["hobbies"][1])   # acess in names to football

# make empty dictionary 
users : dict[key,values] = {}
print(users)
# assign values in users
users[1] = "rao"
users["lname"] = "ali murad"
users["age"] = 19
print(users)

# update value
users["lname"] = "ali" #update
print(users["lname"])

# how can we save code to crash during run time
# print(users["fname"])                       # it give error beacuse in users there is no key of this name
print(users.get('fname',"key is not here")) # its saves to crash program during run time now it print message instead of error
