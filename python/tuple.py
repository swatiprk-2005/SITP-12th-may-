#TUPLE
# tpl=(1,2,3,"hello",1,2) #cretaing tuple
# print("this is my first tuple",tpl)
# print(len(tpl))  #length of my tuple
# print(tpl[2])  #indexing
# print(tpl[:4:1])  #slicing

###TUPLE UNPACKING
# a,b,c=(1,2,3)
# print(a)
# print(b)
# print(c)

# tpl=(1,2,3,"hello",5.5,6)
# print(tpl)  
# print(tpl.count(3))  #count how many times a no. repeats
# print(tpl[3])  #which element is present on given index no.

######for adding any value in tuple
##use type casting
# tpl=(1,2,3,"hello",2)
# print(tpl)
# print(type(tpl))
# print("convert tuple into list")
# a=list(tpl)
# print(a)
# print(type(a))
# a.append(100)
# print(a)
# tpl=tuple(a)
# print(tpl)
# lst= [1,2,"apple","dog"]
# lst.append("cat")
# print(lst)
# lst.remove(2)
# print(lst)
# print(lst[2:4:1])
# tup=(1,2,3,"apple")
# print(tup[3])
# 
# dict={"name":"swati","roll_no":45,"class":23,"address":"jaipur"}
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# Mini Student Management System

# Storing student details using dictionary
student = {
    "name": "Ritik",
    "roll_no": 101,
    "course": "BCA"
}

# Storing subject marks using list
marks = [85, 90, 78, 88, 92]

# Calculating total marks
total = sum(marks)

# Calculating average marks
average = total / len(marks)

# Displaying output
print("===== Student Management System =====")

print("Student Name :", student["name"])
print("Roll Number  :", student["roll_no"])
print("Course       :", student["course"])

print("\nSubject Marks :", marks)

print("Total Marks   :", total)
print("Average Marks :", average)




