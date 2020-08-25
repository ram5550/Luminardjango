lst=[3,4,8]

olst=[]


#sum=3+4+8=15
#  15-3=12
#  15-4=11
# 15-8=7

total=sum(lst)
for element in lst:
    num=total-element
    olst.append(num)
print(olst)