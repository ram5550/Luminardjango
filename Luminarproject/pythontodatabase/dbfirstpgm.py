import mysql.connector   #import mysql connector module
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin='mysql_native_password'

) # estblish connection

#prepare a cursor object using cursor() method.
cursor=db.cursor()

#execute SQL query using execute() method.
sql="SELECT VERSION()"
cursor.execute(sql)

#fetch a single row using fetchone() method.
data=cursor.fetchone()
print("Database version:",data)

#disconnect from server
db.close()