#_______________Импорты________________
from flask import Flask,render_template,url_for,request,flash,redirect, session
import sql
from datetime import datetime
from werkzeug.utils import secure_filename
import os
#_______Регистрация приложения_______
app=Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"]="djsenrbbrvrjsiskssnbeehrhejsn"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = './static/file'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#__Ознакомление с email___
@app.route("/")
def index():
    return render_template("index.html")
 
#______Авторизация пользователя____
@app.route("/login/",methods=["POST","GET"])
def login():
    if request.method=="POST":
       a=sql.authorization_account(request.form["email"],request.form["password"])
       if a:
          session['email']=request.form["email"]
          return redirect(url_for('user'))

          
          
    return render_template("login.html")

#Пользователи
@app.route("/user/",methods=["POST","GET"])
def user():
    return render_template("user.html",email=session["email"])
    



#Создание аккаунта
@app.route("/create/",methods=["POST","GET"])
def create():
    if request.method=="POST":
        sql.create_account(request.form["email"],request.form["password"])
        session['email']=request.form["email"]
        return redirect(url_for('user'))
        
    return render_template("create.html")

@app.route("/user/send",methods=["POST","GET"])
def user_send():
    if request.method=="POST":
        sql.letter(
        session['email'],
        request.form["email_2"],
        request.form["text"],
        request.files["file_1"].filename,
        request.files["file_2"].filename,
        request.files["file_3"].filename,
        request.files["file_4"].filename,
        request.files["file_5"].filename,
        datetime.now()
        )
        file = request.files['file_1']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return render_template("send.html")

   
 
         
            
               
                  
                     
                        
                           
                              
                                 
                                    
                                       
                                          
                                             
                                                
                                                   
                                                      
                                                         
                                                            
                                                               
                                                                  
                                                                     
                                                                           
if __name__=="__main__":
    app.run(debug=True)
    
