# names : list[str] = ["rao","ali","murad","nawaz"]
# print(names)

# alphabets = list("ABCDEFGHIJKL")  #list function

# print(alphabets)


#slice method

# print(names[1:3])
# print(names[0:-1])
# print(names[-3:-1])
# print(names[1::])
# print(names[0::2])

#del
# del names[3] # it does not return it delete permenatly
# print (names)

#pop method

# b = names.pop()      #it return value
# print(b)            #here you can check it print delete value

# print(names.pop(1))    #you can given index number where you want to delete
# print(names)


# without copy method 

# a  : list[str] = ["karachi","lahore","multan","peshwar"]
# # b = a   # assign a to b
# # print(a)
# # print(b)
# # print(a.pop())
# # print(a) # now check it will delete both variable value
# # print(b)  

# # now use copy method

# b = a.copy()
# print(a)
# print(b)

# a.pop()

# print(a) # now only list a element will delete
# print(b)

#  without clear method
# cities : list[str] = ["karachi","multan","Islamabad","lahore"]
# # del cities
# # print(cities) # give error of undefined


# #with clear method
# cities.clear()
# print(cities) # now it give you empty list [] beacuse it will clear value not delelte variable

# append method 

# founders1 : list[str] = ["sir zia","sir ahsan","sir qasim"]
# print(founders1)
# founders1.append("sir ghous") # add value in last
# print(founders1)

# insert method
# founders1 : list[str] = ["sir zia","sir ahsan","sir qasim"]
# founders1.insert(1,"sir ali") # insert value at particular place
# print(founders1)

#count method

# values : list[str] = ['a','b','c','a','a']
# print(values.count('a'))

# extend method 
# founders1 : list[str] = ["sir zia","sir ahsan","sir qasim"]
# founders2 : list[str] = ["sir fahad","sir tahir "]
# founders1.extend(founders2)
# print(founders1)

#remove method 
# founders1 : list[str] = ["sir zia","sir ahsan","sir qasim"]
# founders1.remove("sir qasim")
# print(founders1)

#index method
# founders1 : list[str] = ["sir zia","sir ahsan","sir qasim","sir ahsan"]
# print(founders1.index("sir ahsan"))
# print(founders1.index("sir ahsan",2))






















