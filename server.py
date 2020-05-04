from flask import Flask, redirect, url_for, render_template, request
from dbfuncs import *
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginredir_r',methods = ['POST', 'GET'])
def loginredir_r():
    if request.method == 'POST':
        result = request.form
        if check_user(result["username_r"]) == 0:
            return render_template("user_exists.html")
        else:
            register_user(result["username_r"])
            url = f'/user/{result["username_r"]}/profile'
            return redirect(url)

@app.route('/loginredir',methods = ['POST', 'GET'])
def loginredir():
    if request.method == 'POST':
        result = request.form
        if check_user(result["username"]) == 1:
            return render_template("no_user.html")
        else:
            url = f'/user/{result["username"]}/profile'
            return redirect(url)

@app.route('/user/<user>/search')
def search(user):
    return render_template('search.html', username=user)

@app.route('/user/<user>/searchres')
def searchres(user):
    return render_template('searchres.html', username=user)

@app.route('/user/<user>/profile')
def profile(user):
    return render_template('profile.html', username=user)

@app.route('/user/<user>/pull')
def pull(user):
    return render_template('pull.html',username=user)

@app.route('/user/<user>/builder')
def builder(user):
    return render_template('builder.html')

@app.route('/user/<user>/new_deck')
def new_deck(user):
    return render_template('new_deck.html')

@app.route('/user/<user>/stats')
def stats(user):
    return render_template('stats.html', username=user)

@app.route('/user/<user>/packs')
def packs(user):
    return render_template('packs.html')

@app.route('/user/<user>/pack/<pack_name>')
def edit_pack(user,pack_name):
    return render_template('edit_pack.html')

@app.route('/user/<user>/new_pack')
def new_pack(user):
    return render_template(new_pack)

@app.route('/user/<user>/ccreate')
def ccreate(user):
    return render_template("ccreate.html")


if __name__ == '__main__':
   app.run(debug=True)
