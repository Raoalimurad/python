# names : dict[str,str]  = {"fname":"rao",
#                           "lname":"ali murad",
#                           "education":"student"}
# print("fname" in names.keys())

# a = "ali" not in "rao ali murad is a student"
# print(a)

# align_0 : dict[str,str] = {"color":"green","value":"0"}
# align_1 : dict[str,str] = {"color":"yellow","value":"1"}
# align_2 : dict[str,str] = {"color":"pink","value":"2"}
# align_items =[align_0,align_1,align_2]
# for align in align_items:
#     print(align)

# dictionary methods

names : dict[str,str]  = {"fname":"rao",
                          "lname":"ali murad",
                          "education":"student"}


#1 Acesssing value by key
first_name = names["fname"]
print(first_name)

# 2Modifying Values:

names["education"] = "graduate"
print(names)

#3 Adding Key-Value Pairs:
names["age"] = 19
print(names)

#4 Removing Key-Value Pairs:
del names["lname"]
print(names)

#5 Checking for Key Existence:
if "age" in names:
    print("Age exists in the dictionary.")

#6  Getting a List of Keys and Values
keys = list(names.keys())
print(keys)

# 7 Get a list of values:
values = list(names.values())
print(values)

#8Getting Key-Value Pairs:
items = list(names.items())
print(items)

# clear method :
names.clear()
print(names)

# copy method:
new_dict = names.copy()
print(new_dict)