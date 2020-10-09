
import mysql.connector   #import mysql connector module
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="luminarpython"

) #open database connection

print(db)

#prepare a cursor object using cursor() method.
cursor=db.cursor()

sql="SELECT FIRST_NAME FROM EMPLOYEE WHERE INCOME>=1000"

try:
    cursor.execute(sql)

    myresult=cursor.fetchall()

    for x in myresult:
        print(x)
except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()
