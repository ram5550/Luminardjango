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

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql="CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20),LAST_NAME CHAR(20),AGE INT,SEX CHAR(1),INCOME INT)"

cursor.execute(sql)

db.close()