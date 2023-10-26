a , b , c = "ali", 7 , 3.4 # zip
print(a)
print(b)
print(c)

name = ("murad",90,9.9)

print(name[0],name[1],name[2]) # dont do this

print(*name)# do this

#warlus operator
a: int = 10
if(a < (b := a + 5)):
    print(b)
else:
    print("not found")
