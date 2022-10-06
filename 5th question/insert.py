import sqlite3
conn=sqlite3.connect("sqlite.db")
# I have Insert data one by one in sqlite3
ins='''
    insert into Employee (st_id,st_Employee_name) VALUES('1','Bivash'),
    
    insert into Department (st_id,st_Department_name) VALUES('1','Cloud Engineer')
    
    insert into Project (st_id,st_Project_name) VALUES('2','CI/CD')
    
'''

conn.execute(ins)
conn.commit()
conn.close()