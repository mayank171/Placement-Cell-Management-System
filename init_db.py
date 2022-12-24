import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users ( fullname varchar(100),'
                                   'username varchar(50) PRIMARY KEY,'
                                   'password varchar(255),'
                                   'email varchar(50));'
                                 )



cur.execute('DROP TABLE IF EXISTS Student;')
cur.execute('CREATE TABLE Student (regNo varchar(10) PRIMARY KEY,'
                                 'firstName varchar (150),'
                                 'lastName varchar (50),'
                                 'dob date,'
                                 'email varchar(40),'
                                 'phoneNo bigint,'
                                 'address varchar (200),'
                                 'gender char(1),'
                                 'type varchar (5),'
                                 'cgpa float(2),'
                                 'fa varchar(100),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )



#UG Table
cur.execute('DROP TABLE IF EXISTS UG;')
cur.execute('CREATE TABLE UG (regNo varchar(10) PRIMARY KEY,'
                                 'branch varchar(100),'
                                 'semester int,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )




#PG Table
cur.execute('DROP TABLE IF EXISTS PG;')
cur.execute('CREATE TABLE PG (regNo varchar(10) PRIMARY KEY,'
                                 'branch varchar(100),'
                                 'semester int,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )


#Job TABLE
cur.execute('DROP TABLE IF EXISTS Job;')
cur.execute('create table Job(job_Id varchar(50),'
                                'company varchar(50),'
                                'position varchar(40),'
                                'eligibility varchar(1000),'
                                'cgpa float,'
                                'loc varchar(50),'
                                'type varchar(20),'
                                'primary key(job_Id) );'
                                )

#fulltime TABLE
cur.execute('DROP TABLE IF EXISTS fulltime;')
cur.execute('create table fulltime( job_Id varchar(50),'
                                    'bond varchar(20),'
                                    'package int,'
                                    'primary key(job_Id));'
                                    )

#Internship TABLE
cur.execute('DROP TABLE IF EXISTS internship;')
cur.execute('create table internship( job_Id varchar(50),'
                                    'duration varchar(20),'
                                    'ppo varchar(20),'
                                    'salary int,'
                                    'primary key(job_Id));'
                                    )



cur.execute('DROP TABLE IF EXISTS stats;')
cur.execute('CREATE TABLE stats( regno varchar(100) PRIMARY KEY,'
                                   'job_id varchar(50));'
                                 )


cur.execute('DROP TABLE IF EXISTS applied;')
cur.execute('CREATE TABLE applied( regno varchar(100) PRIMARY KEY,'
                                   'companies varchar(500));'
                                 )





conn.commit()

cur.close()
conn.close()

