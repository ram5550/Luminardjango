f=open("complete.csv","r")
dict={}


for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirm=data[4]
    recovered=data[6]
    death=data[5]
    if(state not in dict):
        dict[state]={"confirm":confirm,"recovered":recovered,"death":death}
    else:
        dict[state] = {"confirm": confirm, "recovered": recovered,"death": death}

def Fetchdata(**kwargs):
    state=(kwargs["state"])
    if (state not in dict):
        print("NO STATE FOUND")
    else:
        for k,val in dict.items():
            if(k==kwargs["state"]):
                print("Total cases:",val["confirm"])
                if "parameter" in kwargs:
                    v=kwargs["parameter"]
                    if (v=="recovered"):
                        print("Recovered:",val["recovered"])
                    elif(v=="death"):
                        print("Death:",val["death"])

Fetchdata(state="Kerala",parameter="death")
