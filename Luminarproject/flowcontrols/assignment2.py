 #Date of birth


bdate=int(input("enter your birth date"))
bmonth=int(input("enter your birth month"))
byear=int(input("enter your birth year"))


curdate=int(input("enter current date"))
curmonth=int(input("enter current month "))
curyear=int(input("enter current year"))

#bday 26-08-2019
#cday 24-07-2020

age=curyear-byear

if(bmonth>=curmonth):

    age=age-1
if(bmonth==curmonth):
    if(bdate>curdate):
        age=age-1

print("you are",age,"years old")