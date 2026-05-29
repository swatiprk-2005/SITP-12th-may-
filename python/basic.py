# print("hello world") 
# x=34
# y=32
# print(type(x))
# x=y=z="orange"
# print(x)
# print(y)
# print(z)
# a="ABC"
# x="A"
# y="B"
# z="C"
# print(x)
# print(y)
# print(z)

# #variable --variables are containers for storing data variables
# # var name must start with a letter  

# myvar="john"
# my_var="swati"
# _my_var="hello"
# myvar="john"
# MYVAR="john"
# myvar2="john"

# #print() pretty flexible you can enter any

# print(34)
# print("salman khan")

# #print(salman khan) not  intilizaed so error

# print("salman kahn",34,24.4,True)
# print("divya",56,"radhika")
# print("hello kahan se ho",end=" ")
# print("mai jaipur se hu")
# print("hello",end="-")
# print("world")
# print("hello"); print("world"); print("i'm ok")
# print(x,y,z)

# #dynamic typing--- c, c++ languages you have totell that the datatype before giving value to
# # int a=20

# x=56
# print(x)
# print(type(x))

# #dynmaic binding == in python there is no fix datatype

# a=45
# print(a)
# a="divya"
# print(a)
# a=int("54")
# print(a)
# print(type(a)) #casting

# ##many values to many variables --python allows you to assign values to multiple variables in one line

# x,y,z="apple","orange","kiwi"
# print(x)
# print(y)
# print(z)
# x=y=z="apple"
# print(x)
# print(y)
# print(z)

# #unpack a collection --if you have a collectio of values in a list, tuple etc
# #python allows youtoextract the values into varibles
# #lists unpacking

# a=["divya","apple","juice"]
# x,y,z=a
# print(x)
# print(y)
# print(z)

# #tuple unpacking
# x=(3,4,5)
# a,b,c=x
# print(a,b,c)

# #string unpacking
# name="ABC"
# a,b,c=name
# print(a,b,c)
# x="python"
# y="is"
# z="good"
# print(x,y,z)
# print(x+y+z)

# #typecasting-- if you want to specify the data type of a varible, this can be done with type casting
# x=int(3)
# y=float(3)
# z=str(3)
# print(x)
# print(y)
# print(z)
# print(type(z))
# ##type conversio ---you can convert from one type to another with the inr(),float(),string()
# #1. implicit type conversion ---interanlly know the dtype

# print(6+6.8)
# print(type(6),type(6.8))

# #2.explicit typeconversion -- program req to chng dtype

# x=float(28)
# print(x)
# #user input---
# #static VS dynamic s/w --static talk with user they only give information
# ##dynamic --user input deta hai(ex--youtube,ola,zomato)
# #a=input("what is your name:-")
# b=input("what is your age:-")
# print(a)
# print(b)

# a=int(input("enter a first number:-"))
# b=int(input("enter second number:-"))
# print(a+b)

# name=input("apna naam btao:-")
# print("hello",name)

# a = int(input("enter a no."))
# b=int(input("enter second no."))
# sum=a*b
# print("total", sum)
# #swappin of two numbers
# a=20
# b=12
# a,b=b,a
# print("A:",a)
# print("B:",b)
# a=20
# b=23
# c=13
# print("A:",a)
# print("B:",b)
# print("C:",c)
# #string rules-
# #1.sequence of characters written inside a quote
# #2.includes letters ,numbers and spaces
# #3.strigs are immutable/uncahnged
# #4.manipulate strigs-like concatenation,formatting,slicing
# #5.delete an entire string variable(python dont delete an individual cahracter)
# a="hello"
# print(a)

# b="python is good"
# print(b)

# c = '''hey how are you
# sb acha
# main thik hu'''
# print(c)
# a=12.3,2.4,3.2
# b=12.3,2.4,3.2
# print(a is b)

# a = 10.5
# b = 10.5
# print(a is b)
