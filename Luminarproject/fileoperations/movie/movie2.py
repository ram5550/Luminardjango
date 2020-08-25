f=open("movies.csv","r")
dict={}
lst=[]

for lines in f:
    #print(lines)
    #break
    data=lines.rstrip("\n").split(",")
    movies=data[1]
    year=data[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
for k,v in dict.items():
    lst.append(int(v))
for k, v in dict.items():
    if(max(lst)==v):
        print("Maximum number of movies released in",k,"-",v,"Movies")