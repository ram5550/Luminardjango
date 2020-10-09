import mysql.connector   #import mysql connector module
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="luminarpython"

) #open database connection



#prepare a cursor object using cursor() method.
cursor=db.cursor()


sql="INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES('VINAY','DEV',24,'M',15000)"
try:
    cursor.execute(sql)
    db.commit()

except Exception as e:
    db.rollback() #partial changes are undone
    print(e.args)

finally:
    db.close()