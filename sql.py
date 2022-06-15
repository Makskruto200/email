import sqlite3 as sq
from datetime import datetime
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

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
                bouk=generate_random_string(16)
                cur.execute(f"""INSERT INTO  letter VALUES ("{email}","{email_2}","{text}","{file_1}","{file_2}","{file_3}","{file_4}","{file_5}","{data}","{bouk}")""")
   except:
       pass


def letter_my(email):
   try:
   
            with sq.connect("users.db") as con:
                cur=con.cursor()
                a= [i for i in cur.execute(f"SELECT * FROM letter WHERE sender='{email}' ")]
                return a
   except:
                return False
                
def letter_read(email,token):
    try:
   
            with sq.connect("users.db") as con:
                cur=con.cursor()
                a= [i for i in cur.execute(f"SELECT * FROM letter WHERE sender='{email}' AND id='{token}'")]
                return a
    except:
                return False
    

