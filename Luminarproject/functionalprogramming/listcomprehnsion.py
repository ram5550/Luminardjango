#list comprehension=single line output
lst=[1,2,3,4,5]

#sqr
sq=[(i*i)for i in lst]
print(sq)

#pairs
pairs=[(i,j) for i in lst for j in lst]
print(pairs)

#even
even=[i for i in lst if i%2==0]
print(even)