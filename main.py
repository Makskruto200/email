#_______________Импорты________________
from flask import Flask,render_template,url_for,request,flash,redirect, session
import sql

#_______Регистрация приложения_______
app=Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"]="djsenrbbrvrjsiskssnbeehrhejsn"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
    return f"{session['email']}"
    



#Создание аккаунта
@app.route("/create/",methods=["POST","GET"])
def create():
    if request.method=="POST":
        sql.create_account(request.form["email"],request.form["password"])
        session['email']=request.form["email"]
        return redirect(url_for('user'))
        
    return render_template("create.html")


   
      
         
            
               
                  
                     
                        
                           
                              
                                 
                                    
                                       
                                          
                                             
                                                
                                                   
                                                      
                                                         
                                                            
                                                               
                                                                  
                                                                     
                                                                           
if __name__=="__main__":
    app.run(debug=True)
    
