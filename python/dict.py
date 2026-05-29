# student={"name":"swati",
# "branch":"CSE",
# "roll_no":34,
# "address":"near sk clg",
# "class":"2nd year"}
#name,branch,roll_no,address,class>>>>>>>>>>>keys
#swati,CSE,34,near sk clg,2nd year>>>>>>>>>>>value
#key + value = item>>>>>>>>
#>>>>>>>>keys are unique so no duplicted values
#>>>>>>>>values can be dupicated
# print(student)
# print("dict keys>>",student.keys())
# print("dict values>>",student.values())
# print("dict item>>",student.items())
# print(student["name"])>>>>>>#for valueof individual key

#>>>>>>>>ADD ITEM IN PYTHON DICT<<<<<<<<<<<
#  print(['subject'])='python'
#TASK1: update and from

# print(student.get('name'))
# print(student.copy())
# print(student.clear())
# print(student.pop('name'))
# print(student.popitem())

#>>>>>>SET DEFAULT
# car= {
# "brand":["ford","honda","hero"],    #multiple values
# "model":"mustang",
# "year":2030 }
# print(car)
# x=car.setdefault("colour","white")
# print(x)

##updation without update
# car=[("year")]=2000
# print(car)

#LOOP
#>>>>>FOR LOOP<<<<<<<<
# for x in car.items():
#     print(x)
# for x in car.keys():
#     print(x)
# for x in car.values():
#     print(x)        

##### SET
#difference b/w dicscard and remove
# a={1,2,3,4}
# a.discard('h') #if it dont find the given value in set, still it prints the set as it is and dont give any error
# print(a)
# a.remove('h') #it gives error when the value is not present in the given set
# print(a)

