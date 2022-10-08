from flask import render_template, request, redirect
from flask_app import app
# Bring user model into these controller routes
from flask_app.models.user_model import User

@app.route('/')
def index():
    return redirect('/new_user')

@app.get('/new_user')
def users():
    return render_template('Create.html')

@app.post('/process')
def add_user():
    print(request.form)
    User.save(request.form)
    return redirect('/show_users')

@app.get('/show_users')
def show_all_users():
    return render_template('Read.html', users=User.find_all())
    

