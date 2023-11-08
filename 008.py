# set data type
data : set = {1,1,1,2,3,2,4,5}
print(data) # return unique

# here you can not access set data type that's why i convert set data type into list data type then you can access the value of set using list

data_type :list= list(set(data))
print(data_type[0]) # access value

for data in data_type:
    print(data)


