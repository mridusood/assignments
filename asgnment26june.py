import sqlite3
#ques1
call=sqlite3.connect('h.db')
print("opened databse successfully")

#call.execute( '''Create table BOOKS(BookId INT PRIMARY KEY NOT NULL,TitleId INT,Location varchar(30),Genre VARCHAR(10));''')

#call.execute('''Create table Title(TitleId int primary key,Title varchar(35),ISBN int,Publisher_ID int,Publication_Year int);''')

#call.execute('''Create table PUBLISHER(Publisher_ID int primary key,Name varchar(15),Street_Address varchar(50),
    #Suite_Number int,Zip_Code_ID int);''')

#call.execute('''Create table Zip_Code(Zip_Code_ID int primary key,City varchar(15),State varchar(20),Zip_Code int);''')
#call.execute('''Create table Author(AuthorID int primary key,FirstName varchar(15),MiddleName varchar(15),LastName varchar(15));''')
#call.execute( '''Create table Author_Titles(Author_Title_ID int primary key,AuthorID int ,TitleId int );''')

#print('Table Created')
#ques2
#call.execute("INSERT INTO BOOKS(BookId,TitleId,Location,Genre) VALUES (1, 01,'abc1', 'physics')")
#call.execute("INSERT INTO BOOKS(BookId,TitleId,Location,Genre) VALUES (2, 02, 'def1','chemistry')")
#call.commit()
#print("inserted")

cursor=call.execute("SELECT BookId,TitleId,Location,Genre from BOOKS")
for row in cursor:
    print("BookId =", row[0])
    print("TitleId =", row[1])
    print("Location =", row[2])
    print("Genre =", row[3], "\n")
print("records created")

#call.execute("INSERT INTO Title(TitleId,Title,ISBN,Publisher_ID,Publication_Year) VALUES ( 01, 'abc',5432,109,1997)")
#call.commit()
#print("insert")

curs=call.execute("SELECT TitleId,Title,ISBN,Publisher_ID,Publication_Year from Title")
for row in curs:
    print("TitleId =", row[0])
    print("Title =", row[1])
    print("ISBN =", row[2])
    print("Publisher_ID =", row[3])
    print("Publication_Year =", row[4], "\n")
print("records created")

#call.execute("INSERT INTO PUBLISHER(Publisher_Id,Name,Street_Address,Suite_Number,Zip_Code_ID) VALUES ( 30, 'john',45,545,111)")
#call.commit()
#print("insertrd!!")
cur=call.execute("SELECT Publisher_Id,Name,Street_Address,Suite_Number,Zip_Code_ID from PUBLISHER")
for row in cur:
    print("Publisher_ID =", row[0])
    print("Name =", row[1])
    print("Street_Address =", row[2])
    print("Suite_Number =", row[3])
    print("Zip_Code_ID =", row[4], "\n")
print("records created")

#call.execute("INSERT INTO Zip_Code(Zip_Code_ID,City,State,Zip_Code) VALUES ( 111, 'amritsar','punjab',51)")
#call.commit()
#print("done")
cur=call.execute("SELECT Zip_Code_ID,City,State,Zip_Code from Zip_Code")
for row in cur:
    print("Zip_Code_ID =", row[0])
    print("City =", row[1])
    print("State =", row[2])
    print("Zip_Code =", row[3], "\n")
print("records created")

#call.execute("INSERT INTO Author(AuthorID,FirstName,MiddleName,LastName) VALUES ( 50, 'richa','abc','sood')")
#call.commit()
#print("inst")
cu=call.execute("SELECT AuthorID,FirstName,MiddleName,LastName from Author")
for row in cu:
    print("AuthorID =", row[0])
    print("FirstName =", row[1])
    print("MiddleName =", row[2])
    print("LastName =", row[3], "\n")
print("records created")

#call.execute("INSERT INTO Author_Titles(Author_Title_ID ,AuthorID  ,TitleId) VALUES ( 22, 50,01)")
#call.commit()
#print("yes")
cu=call.execute("SELECT Author_Title_ID ,AuthorID  ,TitleId from Author_Titles")
for row in cu:
    print("Author_Title_ID =", row[0])
    print("AuthorID =", row[1])
    print("TitleId =", row[2], "\n")
print("records created")

#ques3
print("original values are:")
cursor=call.execute("SELECT BookId,TitleId,Location,Genre from BOOKS")
for row in cursor:
    print("BookId =", row[0])
    print("TitleId =", row[1])
    print("Location =", row[2])
    print("Genre =", row[3], "\n")
print("records created")
call.execute("UPDATE BOOKS set Genre = 'Maths' where BookId=2")
call.commit()
print("updated values are")
cursor=call.execute("SELECT BookId,TitleId,Location,Genre from BOOKS")
for row in cursor:
    print("BookId =", row[0])
    print("TitleId =", row[1])
    print("Location =", row[2])
    print("Genre =", row[3], "\n")


print("records updated")