import sqlite3 as sq
from datetime import datetime
def authorization_account(email, password):
   try:
            with sq.connect("users.db") as con:
                cur=con.cursor()
                a=[i for i in cur.execute(f"SELECT * FROM users WHERE  email='{email}'")]
                if a[0][2]==str(password):
                    return a[0]
                else:
                    return False
   except:
             return False

def create_account(email,password):
    try:
            with sq.connect("users.db") as con:
                cur=con.cursor()
                cur.execute(f"""INSERT INTO  users (email, password) VALUES ("{email}","{password}")""")
    except:
       pass
def letter(email,email_2,text,file_1,file_2,file_3,file_4,file_5,data):
   try:
            with sq.connect("users.db") as con:
                cur=con.cursor()
                cur.execute(f"""INSERT INTO  letter VALUES ("{email}","{email_2}","{text}","{file_1}","{file_2}","{file_3}","{file_4}","{file_5}","{data}")""")
   except:
       pass
   
