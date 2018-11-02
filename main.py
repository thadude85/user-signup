from flask import Flask, request, redirect
import cgi
import os
import jinja2


template_dir= os.path.join(os.path.dirname(__file__), 'templates')
jinja_env=jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    template=jinja_env.get_template('sign_up_form.html')
    return template.render()

@app.route("/validate",methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    username_error=''
    password_error=''
    verify_password_error=''
    email_error=''


    if ' ' in username:
        username_error='Not a valid username'
        
    else:
        if len(username) <3 or len(username)>20:
            username_error='Enter a username between 3 and 20 characters long'
            
   
    if ' ' in password:
        password_error='Not a valid password'
        password=''

    if len(password) <3 or len(password)>20:
        password_error='Enter a password between 3 and 20 characters long'
        password=''

    if verify_password != password:
        verify_password_error='passwords do not match'
        verify_password=''
    
    if email !='':
        if ' ' in email:
            email_error='Not a valid email'
            
        if '@' not in email:
            email_error='Not a valid email'
            
        if '.' not in email:
            email_error='Not a valid email'
            
        else:
            if len(email) <3 or len(email)>20:
                email_error='Not a valid email'
                
                
    if not username_error and not password_error and not verify_password_error and not email_error:
        
        return redirect('/welcome?username={0}'.format(username))
    else:
        template=jinja_env.get_template('sign_up_form.html')
        return template.render(username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username,email=email,password=password, verify_password=verify_password)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return '<h1>Welcome {0}!</h1>'.format(username)
    
app.run()

    
