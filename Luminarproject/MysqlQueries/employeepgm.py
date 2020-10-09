f=open("employees")
emp={}
for lines in f:
    id,name,desig,salary=lines.rstrip("\n").split(",")
    if (id not in emp):
        emp[id]={"id":id,"name":name,"desig":desig,"sal":salary}

def fetchData(**kwargs):
    #here kwargs is a dictionry
    #key=id
    #value=1001
    id=(kwargs["id"])
    #id=1001
    if(id not in emp):
        print("employee not exist")
    else:
        print(emp[id]["name"])
        # emp[1001]["name"]
        if "prop" in kwargs:
            val=kwargs["prop"]
            print(emp[id][val])


fetchData(id="1001",prop="sal")
