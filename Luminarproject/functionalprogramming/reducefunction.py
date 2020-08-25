import functools
lst=[10,20,30,31,32]
                       #10,20:10+20=30
                       #30,30:30+30=60
                       #60,31:60+31=91
                       #91,32:91+32=123
total=functools.reduce(lambda num1,num2:num1+num2,lst)
print(total)

                           #eg->#30,20:return 30 if 30>20 else return 20
maxval=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(maxval)

minval=functools.reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(minval)