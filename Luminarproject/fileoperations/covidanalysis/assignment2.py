
f=open("covid_19_india.csv","r")
dict={}
dict2={}
maxtotalcases=0
maxdeathcases=0
totalconfirmed=0
totaldeath=0
for lines in f:
    #print(lines)
    #break
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    confirmed=data[8]
    #print(state,",",death)
    if(state not in dict):
        dict[state]=confirmed
    else:
        dict[state]=confirmed
    if(state not in dict2):
        dict2[state]=death
    else:
        dict2[state]=death

print("STATE: CONFIRMED CASES")
for k,v in dict.items():
    print(k,",",v)
    totalconfirmed=totalconfirmed+int(v)
    if int(v)>maxtotalcases:
        maxtotalcases=int(v)
        maxtotalstate=k

print("STATE: DEATH CASES")
for k,v in dict2.items():
    print(k,",",v)
    totaldeath=totaldeath+int(v)
    if int(v)>maxdeathcases:
        maxdeathcases=int(v)
        maxdeathstate=k


print("Total death in India               :",totaldeath)
print("Total confirmed cases in India     :",totalconfirmed)
print("State with highest confirmed cases :",maxtotalcases,"(",maxtotalstate,")")
print("State with highest death cases     :",maxdeathcases,"(",maxdeathstate,")")
