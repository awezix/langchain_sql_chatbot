import sqlite3

# connect to sqllite3
connection=sqlite3.connect("student.db")

# create a cursor object to insert record,create table
cursor=connection.cursor()

# create table
table_info='''
create table Student(Name varchar(25),Class varchar(25),Section varchar(25),Marks int)
'''
cursor.execute(table_info)

cursor.execute('''insert into Student values("krish","Data Science","A",90)''')
cursor.execute('''insert into Student values("John","Data Science","A",100)''')
cursor.execute('''insert into Student values("Mukesh","Data Science","A",86)''')
cursor.execute('''insert into Student values("Jacob","Devops","A",50)''')
cursor.execute('''insert into Student values("Dipesh","Devops","A",35)''')

# display all the records
print("the inserted records are :")
data=cursor.execute('''select * from Student ''')
for row in data:
    print(row)

# commit all changes
connection.commit()
connection.close()