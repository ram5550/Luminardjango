f=open("temperaturedata","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")  #"trivandrum,27
    district=data[0]
    temperature=data[1]

    if(district not in dict):
        dict[district]=temperature
    else:
        old=dict[district]
        if(temperature>old):
            dict[district]=temperature
print(dict)