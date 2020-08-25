#[10,20,30,40]=>squar=>[100,400,900,1600]----->map
#[1,2,3,4,5,6]=>even=>[2,4,6]---->filter


lst=[1,2,3,4]

def square(num):
    return num*num
sq=list(map(square,lst)) #map(function,iterables) here func=sqr and itera=lst
print(sq)


#filter

#filter(function,iterables)

def even(num):
    return num%2==0
even=list(filter(even,lst))
print(even)