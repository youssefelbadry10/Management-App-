#import sqlite module
import sqlite3

#Create Database and connect

db = sqlite3.connect("app.db")

# Setting up the cursor
cr = db.cursor()


#Creat table and fields

cr.execute("CREATE TABLE if not exists skills (name text, progress integer, user_id integer )")
cr.execute("CREATE TABLE if not exists users (user_id integer, name text)")


#inserting Data

cr.execute("insert into users(user_id, name) values(1, 'youssef')")
cr.execute("insert into users(user_id, name) values(2,' khaled')")
cr.execute("insert into users(user_id, name) values(3, 'sara')")


#loop to insert persons in database
list = {"ahmed", "ibrahim", "ali"}

for key,i in enumerate(list):
    cr.execute(f"insert into users(user_id, name) values({key + 4}, '{i}')")


# Save Commit changes (commit = the inputs you put )
db.commit()

#close Database
db.close()
