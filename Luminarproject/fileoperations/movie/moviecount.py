
f=open("movies.csv","r")
dict={}
dict1={}
dict2={}
mlst=[]

for lines in f:
    #print(lines)
    #break
    data=lines.rstrip("\n").split(",")
    movies=data[1]
    year=data[2]
    rate=data[3]

    if(movies not in dict):
        dict[movies]=year

    else:
        dict[movies]=year

    if year not in dict1:
        dict1[year]=1

    else:
        dict1[year]+=1

    if(rate not in dict2):
        dict2[rate]=1

    else:
        dict2[rate]+=1



for k,v in dict1.items():
    print(k,",",v)

for k,v in dict1.items():
    mlst.append(int(v))
for k, v in dict1.items():
    if (int(v)==max(mlst)):
        myear=k
        mcount=int(v)

print(myear,"has max number of movies",mcount)


for k,v in dict2.items():
    print(k,",",v)