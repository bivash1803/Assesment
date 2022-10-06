import sqlite3
conn=sqlite3.connect("sqlite.db")
# I have created table one by one please check all the table in online sql
conn.execute('''
             Create table Department (
            st_id INT AUTO_INCREMENT PRIMARY KEY,
            st_Department_name VARCHAR(50)
            )
            Create table Project (
            st_id INT AUTO_INCREMENT PRIMARY KEY,
            st_Project_name VARCHAR(50)
            )
            Create table Employee (
            st_id INT AUTO_INCREMENT PRIMARY KEY,
            st_Employee_name VARCHAR(50)
            )
    ''')

conn.close()