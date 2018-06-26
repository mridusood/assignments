#DATABASES
#select * from tbname where id='2'
#Insert into tbname(id,age) vlaues('2','19')
import sqlite3

conn=sqlite3.connect('test.db')
print("opened databse successfully")

#conn.execute('''Create Table Company (
#ID INT PRIMARY KEY NOT NULL,
#NAME TEXT NOT NULL,
#AGE INT NOT NULL,
#ADDRESS CHAR(50),
#SALARY REAL);''')
#print("Table created")

#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (59, 'Paul', 32, 'California', 20000)")
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (60, 'hana', 34, 'California', 15000)")
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (61, 'john', 30, 'Brampton', 20000)")
#conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (62, 'Paul', 34, 'New York', 20000)")
#conn.commit()
#print("Inserted")

cursor=conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3], "\n")
print("records created")

conn.execute("UPDATE COMPANY set SALARY = 50000 where ID = 59")
conn.commit()
cursor=conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3], "\n")
print("records created")

conn.execute("DELETE from COMPANY where ID = 60")
conn.commit()
cursor=conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3], "\n")
print("records created")
