from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,length
from flask_bootstrap import Bootstrap5


'''
Read Flask-WTF Quickstart - Creating Forms :-https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 


'''


class Myform(FlaskForm):
    email=StringField(label='Email',validators=[DataRequired(),Email()])
    password=PasswordField(label="Password",validators=[DataRequired(),length(min=8)])
    submit=SubmitField(label="Log In")

app = Flask(__name__)

bootstrap = Bootstrap5(app) # initialise bootstrap-flask 
app.secret_key="anystring"




@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login" ,methods=["GET","POST"])
def login():
    login_form=Myform()
    if login_form.validate_on_submit():
        if login_form.email.data=="admin@email.com" or login_form.password.data=="12345678":
            return render_template("success.html")
        
        return render_template("denied.html")
        
    return render_template("login.html",form=login_form)





if __name__ == '__main__':
    app.run(debug=True)
