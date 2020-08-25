#dictionary

dict={}
#datas are stored in the form of key,value pairs

#rol :"ajay"
#key,rol
#value:ajay

student={"rol":1001,"name":"tinu","age":25,"cpp":25}
# print(student["name"])
# print(student["age"])

for key in student:
    print(key,":",student[key])
#updating value

student["cpp"]+=25
print(student)