input1 = int(input("Entre the value of a"))
input2 = int(input("Entre the value of b"))
operator = input("Entre your operator")
if(operator == "+"):
    print(f"the sum of {input1} and {input2} is {input1 + input2}")
elif(operator == "-"):
    print(f"the subtraction of {input1} and {input2} is {input1 - input2}")
elif(operator == "*"):
    print(f"the multiplication of {input1} and {input2} is {input1 * input2}")
elif(operator == "/"):
    print(f"the divison of {input1} and {input2} is {input1 / input2}")
elif(operator == "%"):
    print(f"the modules of {input1} and {input2} is {input1 % input2}")
else:
    print("entre a vaild operator or value")



