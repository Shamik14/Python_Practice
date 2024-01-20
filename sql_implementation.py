import _sqlite3

conn = _sqlite3.connect("users.db")
print("Database created successfully !")

conn.execute('create table if not exists emp (emp_id int,emp_name char(20),emp_salary int)')
print("Table created successfully !")

conn.execute("insert into emp values(1,'Ankur',10000)")
conn.execute("insert into emp values(2,'Ruchika',3000)")
conn.execute("insert into emp values(3,'Sakshi',11000)")
conn.execute("insert into emp values(4,'Deepak',7000)")
conn.execute("insert into emp values(5,'Pankaj',15000)")
print("Records inserted successfully !")
conn.commit()

#DDL : Data definition language
#DML : Data manipulation language
