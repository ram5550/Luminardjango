

low=int(input("enter low"))

upp=int(input("enter upper limit"))
evensum=0
oddsum=0
for i in range(low,(upp+i)):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i

print(evensum)
print(oddsum)